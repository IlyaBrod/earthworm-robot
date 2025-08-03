# Copyright (c) 2024 I. Brodoline. See LICENSE file for details.

import Mathematiks as mt
import numpy as np
import matplotlib.pyplot as plt

class robotModel():

    robot_index = 0

    def __init__(self,radius: float, AR: float, profile: str,**options) -> None:
        """Create a robot model, based on tip parameters

        Args:
            radius (float): [mm] radius of the robot body
            AR (float): aspect ratio of the tip shape (ratio = L/D)
            profile (string): name of the tip profile model ("VonKaraman", "Cone")
            **options: "name" (string), "body_length" [mm]
        """
        #default settings
        self.body_length = 0
        self.name = ""

        for key, value in options.items():
            match(key):
                case "body_length":
                    self.body_length = float(value)
                case "name":
                    self.name = value
                
        
        self.name += str(robotModel.robot_index)
        self.tip_radius = radius
        self.tip_AR = AR
        self.tip_profile = profile
        self.tip_length = AR*2*radius

        self.robot_index = robotModel.robot_index
        robotModel.robot_index +=1

    def print(self):
        print("#" + self.name)
        print("R [mm]: " + str(self.tip_radius) + " | AR: " + str(self.tip_AR))
        print("BODY length [mm]:" + str(self.body_length) + " | TIP length [mm]: " +str(self.tip_length))

    def getLength(self):
        return self.tip_length + self.body_length

    def getProfile(self,*argv,**options):
        """Calculates the tip profile function.
        Automatically along all the tip lengtg, or only in the point "coord"

        Args:
            *argv: "plot" - displays the curve
                   "coord" - specify the point
            **options: "resolution=X" - X number of values

        Returns:
            vec_y (float_array, float_array): function result y vector and x vector
        """

        plot = False
        res = 1000
        coord = None
        body = None

        #Get the options
        if "plot" in argv:
            plot = True
        
        for key, value in options.items():
                match(key):
                    case "resolution":
                        res = int(value)
                    case "coord":
                        coord= options["coord"]

        #Get curve shape
        if(coord is None):
            vec_x = np.linspace(0, self.tip_length + self.body_length, num=res)
        else:
            vec_x = coord

        vec_y = np.zeros(np.size(vec_x))

        if(coord is None):
            for i in range(np.size(vec_x)):
                if(vec_x[i] < 0):
                    vec_y[i] = 0
                elif(vec_x[i] <= self.tip_length):
                    match(self.tip_profile):
                        case "VonKaraman":
                            vec_y[i] = mt.fx_VonKaraman(vec_x[i], self.tip_length,self.tip_radius*2)
                        case "Cone":
                            vec_y[i] = mt.fx_cone(vec_x[i], self.tip_length,self.tip_radius*2)
                        case _:
                            raise Exception('Unknown function model: ' + type)
                else:
                    vec_y[i] = self.tip_radius
        else:
            if(vec_x < 0):
                vec_y = 0
            elif(vec_x <= self.tip_length):
                match(self.tip_profile):
                    case "VonKaraman":
                        vec_y = mt.fx_VonKaraman(vec_x, self.tip_length,self.tip_radius*2)
                    case "Cone":
                        vec_y = mt.fx_cone(vec_x, self.tip_length,self.tip_radius*2)
                    case _:
                        raise Exception('Unknown function model: ' + type)
            else:
                vec_y = self.tip_radius
                

        if(plot):
            plt.figure()
            plt.plot(vec_x,vec_y,color="black")
            plt.plot(vec_x,-vec_y,color="black")
            plt.xlabel('X [mm]')
            plt.ylabel('Y [mm]')
            plt.title("#" + self.name + ' TIP Profile: ' + self.tip_profile + " AR:" + str(self.tip_AR))
            plt.grid(which='both')
            plt.draw()

        return vec_y



        