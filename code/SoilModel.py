# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

import pandas as pd 
import numpy as np
import Mathematiks as mt
import matplotlib.pyplot as plt
from CONFIG import*
from typing import Any, List, Tuple

class SoilModel():

    def __init__(self,name: str,**options) -> None:
        """_summary_

        Args:
            name (str): name of the soil type
            **options : friction [deg], interface_friction [deg], particle_density [kg/m^3],
            void_index, bulk_density [kg/m^3]
        """
        
        self.name = name

        self.friction = None # Friction angle of the soil [deg]
        self.interface_friction = None # Friction angle with the interface material [deg]

        self.water_unit_weight = WATER_UNIT_WEIGHT # [kN/m^3]
        self.bulk_density = None
        self.rho = None #particle density [kg/m^3]
        self.void_ratio = None
        self.e_max = None
        self.e_min = None
        self.Dr = None #[%] relative density
        self.D = None #[mm] Tank diameter, None : infinite
        self.H = None #[mm] Tank height, None : infinite
    
        #Get the **options
        for key, value in options.items():
                match(key):
                    case "interface_friction":
                        self.interface_friction = float(value)
                    case "friction":
                        self.friction = float(value)
                    case "particle_density":
                        self.rho = float(value)
                    case "bulk_density":
                        self.bulk_density = float(value)
                    case "void_ratio":
                        self.void_ratio = float(value)
                    case "e_min":
                        self.e_min = float(value)
                    case "e_max":
                        self.e_max = float(value)
                    case "tank_D":
                        self.D = float(value)
                    case "tank_H":
                        self.H = float(value)

        #Pre-calculations from known data
        if(self.bulk_density != None):
            self.solid_unit_weight = G_CONSTANT*self.bulk_density/1000

            if(self.rho != None and self.D != None and self.H != None):
                V_total = np.pi * (self.D*1e-3/2)**2 * self.H*1e-3
                M_solid = self.bulk_density * V_total
                print("M_solid ",M_solid)
                V_solid = M_solid / self.rho
                print("V_solid ",V_solid)
                print("V_total ",V_total)
                V_void = V_total - V_solid
                self.void_ratio = V_void/V_solid
                self.Dr = (self.e_max - self.void_ratio)/(self.e_max - self.e_min)*100
                print("Dr [%] = ",self.Dr, " e = ",self.void_ratio)

        elif(self.rho != None and self.void_ratio != None):
            self.solid_unit_weight = G_CONSTANT* self.rho * (1-self.void_ratio) /1000
        else:
            self.solid_unit_weight = None
        

    def getVerticalConstraint(self,z):
        """ Returns soil normal stress [kN/m^2]"""
        if(self.solid_unit_weight is None):
            raise Exception('Soil density not defined - material: ' + self.name)
        else:
            return self.solid_unit_weight * z

    def getHorizontalConstraint(self,z):
        return self.getVerticalConstraint(z)* (1 - np.sin(np.radians(self.friction)))

    def __poreWaterPressure(self,z):
        """ Returns pore water pressure [kN/m^2]"""
        return self.water_unit_weight*z

    def __effectiveStress(self,sigma,u):
        """_summary_

        Args:
            sigma (float): total normal stress
            u (float): pore water pressure

        Returns:
            flaot: effective normal stress
        """
        return sigma - u

    def getInterraction(self,toolModel, dZ,**options) -> pd.DataFrame:
        """Give soil - penetration tool interractions.

        Args:
            toolModel (RobotModel): Penetration tool model
            dZ (float): penetration depth[mm]

            **options (Any): z0 - starting depth [mm] 
                             resolution - number of simulation points (default: 1000)
                             zforce - provide a vector with the z force [N]
                             zdepth - provide a vector with the vertical position [mm]

        Returns:
            Tuple[List[int], List[int]]: vec_depth [mm], vec_sigma_z [kPa], vec_newton_z [N], vec_skinFriction [N]
        """

        #Get the **options
        z0 = options.get('z0', 0)
        res = options.get("resolution",1000)

        #define profile func
        fx_profile = lambda x: toolModel.getProfile(coord=x)

        #define sigma_z [Pa]
        tool_length = (toolModel.tip_length + toolModel.body_length) #value in [mm]
        dZ = np.min([dZ, tool_length]) #limit penetration length to tool length
        vec_z = np.linspace(z0,dZ+tool_length,res) #penetration depth vector in [mm] !Offset of tip_length
        len_z = np.size(vec_z)
        vec_sigma_z = self.getVerticalConstraint((vec_z-tool_length)*1e-3)*1e3 # vector in [Pa]
        vec_sigma_x = np.zeros(np.size(vec_sigma_z))
        len_tip = np.size(vec_sigma_z[vec_sigma_z<0])
        vec_sigma_z[vec_sigma_z<0] = 0 #sigma_z null outside the ground  level

        #define tool tip caracteristics [m, m**2, rad]
        vec_tool_profile = np.zeros(len_tip) #radius of the tip
        vec_tool_profile[0] = fx_profile(vec_z[0])*1e-3
        vec_tool_area = np.zeros(len_tip) #section area of the tip
        vec_tool_areaLateral = np.zeros(len_tip) #lateral projected area of the tip
        vec_tool_surface = np.zeros(len_tip) #lateral surface area of the tip
        vec_tool_surfaceAngle = np.zeros(len_tip) #lateral surface angle [0rad : horizontal surface, pi/2 : vertical, trigo. direction]

        for i in range(1,len_tip): #generating geometry description data
            vec_tool_profile[i] = fx_profile(vec_z[i])*1e-3
            vec_tool_area[i] = np.abs(np.pi*(vec_tool_profile[i]**2))# - vec_tool_profile[i-1]**2)
            vec_tool_areaLateral[i] = np.abs(2 * np.pi * vec_tool_profile[i] * (vec_z[1]-vec_z[0])*1e-3) 
            vec_tool_surface[i] = mt.frustrumIntegral(fx_profile,[vec_z[i-1], vec_z[i]])*1e-6
            vec_tool_surfaceAngle[i] = np.pi/2 - mt.frustrumAngle(fx_profile,[vec_z[i-1], vec_z[i]])

        #calculating forces and sleeve friction [N]
        len_force = len_z - len_tip + 1
        vec_newton_z = np.zeros(len_force)
        vec_newton_x = np.zeros(len_force)
        vec_skinFriction = np.zeros(len_force)

        if(self.friction is not None):
            vec_sigma_x = vec_sigma_z * (1 - np.sin(np.radians(self.friction)))
        if(self.interface_friction is not None):
            friction_coeff = np.tan(np.radians(self.interface_friction))
        else:
            friction_coeff = 0

        for zi in range(0,len_force): #penetration step
                for i in range(0,len_tip):
                    temp_d = vec_tool_profile[i]*2+1e-10 #1e-10 to avoid zero division
                    if(self.Dr != None): #Boundary conditions correction factor
                        corr = 1/np.float_power( (self.D*1e-3/temp_d - 1)/70,self.Dr/200)
                        #print("Correction tank / field = : ",corr)
                    else:
                        corr = 1
                    temp_force_z = vec_sigma_z[zi+len_tip-i-1] * vec_tool_area[i] * corr
                    temp_force_x = vec_sigma_x[zi+len_tip-i-1] * vec_tool_areaLateral[i]

                    temp_a = vec_tool_surfaceAngle[i]
                    temp_force_norm = temp_force_x * np.cos(np.pi/2 - temp_a) \
                                    +temp_force_z * np.cos(temp_a)
                    temp_force_norm *= np.cos(np.pi/2 - temp_a) #proj on z axis
                    temp_force_norm *= friction_coeff #convert to friction

                    vec_newton_z[zi] += temp_force_z
                    vec_newton_x[zi] += temp_force_x
                    vec_skinFriction[zi] += temp_force_norm

        #format output vectors
        vec_depth = vec_z[len_tip-1:] - vec_z[len_tip-1]
        vec_sigma_z = vec_sigma_z[len_tip-1:]/1000 #to kPa
        vec_sigma_x = vec_sigma_x[len_tip-1:]/1000 #to kPa
        # print("vec_sigma_z: ",np.size(vec_sigma_z))
        # print("vec_depth: ",np.size(vec_depth))

        return_table = {
            "depth": vec_depth,
            "sigma_z" : vec_sigma_z,
            "sigma_x" : vec_sigma_x,
            "force_z" : vec_newton_z,
            "force_x" : vec_newton_x,
            "skinFriction" : vec_skinFriction,
            # "toolSurface" :  pd.Series([vec_tool_surface]),
            # "toolSurfaceAngle" :  pd.Series([vec_tool_surfaceAngle]),
            # "toolArea" :  pd.Series([vec_tool_area]),
            # "toolProfile" :  pd.Series([vec_tool_profile]),
            # "toolIndex" : pd.Series([len_tip])
        }

        return_table = pd.DataFrame(return_table)

        return return_table


    # def getInterractionFromData(self,toolModel,zdepth, zforce,**options) -> Tuple[List[int], List[int]]:
    #     """Give soil - penetration tool interractions.

    #     Args:
    #         toolModel (RobotModel): Penetration tool model
    #         zforce - provide a vector with the z force [N]
    #         zdepth - provide a vector with the vertical position [mm]            

    #     Returns:
    #         Tuple[List[int], List[int]]: vec_depth [mm], vec_sigma_z [kPa], vec_newton_z [N], vec_skinFriction [N]
    #     """

    #     #Get the **options
    #     z0 = zdepth[0]
    #     res = options.get("resolution",1000)

    #     #define profile func
    #     fx_profile = lambda x: toolModel.getProfile(coord=x)

    #     #define sigma_z [Pa]
    #     tool_length = (toolModel.tip_length + toolModel.body_length) #value in [mm]
    #     step_z = zdepth[1] - zdepth[0]
    #     vec_z = zdepth
    #     len_z = np.size(vec_z)
    #     len_tip = toolModel.getLength()//step_z
    #     tip_z = np.linspace(0,toolModel.getLength(),len_tip)

    #     #vec_sigma_z = self.getVerticalConstraint((vec_z-tool_length)*1e-3)*1e3 # vector in [Pa]
    #     #vec_sigma_x = np.zeros(np.size(vec_sigma_z))
    #     #vec_sigma_z[vec_sigma_z<0] = 0 #sigma_z null outside the ground  level

    #     #define tool tip caracteristics [m, m**2, rad]
    #     vec_tool_profile = np.zeros(len_tip) #radius of the tip
    #     vec_tool_profile[0] = fx_profile(0)*1e-3
    #     vec_tool_area = np.zeros(len_tip) #section area of the tip
    #     vec_tool_areaLateral = np.zeros(len_tip) #lateral projected area of the tip
    #     vec_tool_surface = np.zeros(len_tip) #lateral surface area of the tip
    #     vec_tool_surfaceAngle = np.zeros(len_tip) #lateral surface angle [0rad : horizontal surface, pi/2 : vertical, trigo. direction]

    #     for i in range(1,len_tip): #generating geometry description data
    #         vec_tool_profile[i] = fx_profile(tip_z[i])*1e-3
    #         vec_tool_area[i] = np.abs(np.pi*(vec_tool_profile[i]**2))# - vec_tool_profile[i-1]**2)
    #         vec_tool_areaLateral[i] = np.abs(2 * np.pi * vec_tool_profile[i] * (tip_z[1]-tip_z[0])*1e-3) 
    #         vec_tool_surface[i] = mt.frustrumIntegral(fx_profile,[tip_z[i-1], tip_z[i]])*1e-6
    #         vec_tool_surfaceAngle[i] = np.pi/2 - mt.frustrumAngle(fx_profile,[tip_z[i-1], tip_z[i]])

    #     #calculating forces and sleeve friction [N]
    #     vec_newton_z = np.zeros(len_z)
    #     vec_newton_x = np.zeros(len_z)
    #     vec_skinFriction = np.zeros(len_z)

    #     if(self.friction is not None):
    #         vec_sigma_x = vec_sigma_z * (1 - np.sin(np.radians(self.friction)))
    #     if(self.interface_friction is not None):
    #         friction_coeff = np.tan(np.radians(self.interface_friction))
    #     else:
    #         friction_coeff = 0

    #     for zi in range(0,len_z): #penetration step
    #             for i in range(0,len_tip):
    #                 temp_d = vec_tool_profile[i]*2+1e-10 #1e-10 to avoid zero division
    #                 if(self.Dr != None): #Boundary conditions correction factor
    #                     corr = 1/np.float_power( (self.D*1e-3/temp_d - 1)/70,self.Dr/200)
    #                     #print("Correction tank / field = : ",corr)
    #                 else:
    #                     corr = 1
    #                 temp_force_z = vec_sigma_z[zi+len_tip-i-1] * vec_tool_area[i] * corr j
    #                 temp_force_x = vec_sigma_x[zi+len_tip-i-1] * vec_tool_areaLateral[i]

    #                 temp_a = vec_tool_surfaceAngle[i]
    #                 temp_force_norm = temp_force_x * np.cos(np.pi/2 - temp_a) \
    #                                 +temp_force_z * np.cos(temp_a)
    #                 temp_force_norm *= np.cos(np.pi/2 - temp_a) #proj on z axis
    #                 temp_force_norm *= friction_coeff #convert to friction

    #                 vec_newton_z[zi] += temp_force_z
    #                 vec_newton_x[zi] += temp_force_x
    #                 vec_skinFriction[zi] += temp_force_norm

    #     #format output vectors
    #     vec_depth = vec_z[len_tip-1:] - vec_z[len_tip-1]
    #     vec_sigma_z = vec_sigma_z[len_tip-1:]/1000 #to kPa
    #     vec_sigma_x = vec_sigma_x[len_tip-1:]/1000 #to kPa
    #     # print("vec_sigma_z: ",np.size(vec_sigma_z))
    #     # print("vec_depth: ",np.size(vec_depth))

    #     return_table = {
    #         "depth": vec_depth,
    #         "sigma_z" : vec_sigma_z,
    #         "sigma_x" : vec_sigma_x,
    #         "force_z" : vec_newton_z,
    #         "force_x" : vec_newton_x,
    #         "skinFriction" : vec_skinFriction,
    #         "toolSurface" : vec_tool_surface,
    #         "toolSurfaceAngle" : vec_tool_surfaceAngle,
    #         "toolArea" : vec_tool_area,
    #         "toolProfile" : vec_tool_profile,
    #         "toolIndex" : len_tip
            
    #     }
    #     return return_table
