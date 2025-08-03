# Copyright (c) 2025 I. Brodoline. See LICENSE file for details.
# Figure3 : A Vertical AR1 and AR1 Airflow
#           B Energy Vertical AR1 and AR1 Airflow

from CONFIG import*
from RobotModel import*
from SoilModel import*
from expData.processFunctions import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from expData.verticalExperiments import*
from expData.horizontalExperiments import*

if (__name__ == "__main__"):

    matplotlib.rc('font', **font)
    fig,axs = plt.subplots(2,1,figsize=(6,10)) #
    plt.subplots_adjust(left=.16,right=.95,top=0.85,bottom=0.05,hspace=0.35)

    #Plot AR1, AR1 Airflow
    axs[0].plot(expAR1['z'],expAR1['mean'],color=ColorList2[COLOR_H_AR1+2],label='$AR_1$')
    axs[0].fill_between(expAR1['z'],expAR1['m_std'], expAR1['p_std'], color=ColorList2[COLOR_H_AR1+1], alpha=0.3)

    axs[0].plot(expAIR['z'],expAIR['mean'],color=ColorList[COLOR_AIR],label='Airflow 34kPa')
    axs[0].fill_between(expAIR['z'],expAIR['m_std'], expAIR['p_std'], color=ColorList[COLOR_AIR], alpha=0.3)

    leg = axs[0].legend(loc='upper center',draggable=True,ncol= 2,borderaxespad=0,bbox_to_anchor=(0, 1.2, 1., .102)) 
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    axs[0].grid(which="both")
    axs[0].set_ylabel('Force [N]')
    axs[0].set_xlabel('Depth [mm]')
    #axs[0].minorticks_on()
    axs[0].text(0.01, .87, 'A', fontsize=40,transform=axs[0].transAxes)
    plt.draw()

    #Energy estimation: [AR1, AIR]
    expAR1 = getWork(expAR1)
    expAIR = getWork(expAIR)

    # #Air blowing system 34kPa "constant" pressure 3mm hole diameter
    # At 200mm depth
    AIR_surface = np.pi * (1.5e-3)**2
    PRESSURE_WORK = (34e3 * AIR_surface * 200e-3) #add 3% of motor efficiency loss
    PRESSURE_WORK_VEC = np.array([0,PRESSURE_WORK]) #to manage display
    
    myDepth = 200
    z_index = expAR1[expAR1['z'] < myDepth].index[-1]

    energyFactors = np.array([
        expAR1['W_med'].iloc[z_index], 
        expAIR['W_med'].iloc[z_index], 
    ])

    print(PRESSURE_WORK_VEC)


    colorArray = [
        ColorList2[COLOR_H_AR1+2],
        ColorList[COLOR_AIR]
    ]

    _err = np.array([
        expAR1['W_std'].iloc[z_index],
        expAIR['W_std'].iloc[z_index]
        ])


    #Get friction from simulation
    # fineSand = SoilModel("fine sand",
    #                     bulk_density=SAND_FINE_BULK_DENSITY[SELECT_DENSITY],
    #                     particle_density = SAND_FINE_GRAIN_DENSITY,
    #                     interface_friction = SAND_FINE_INTERFACE_FRICTION,
    #                     friction = SAND_FINE_FRICTION,
    #                     tank_H = TANK_HEIGHT,
    #                     tank_D = TANK_DIAMETER,
    #                     e_min = SAND_FINE_VOIDRATIO_MIN,
    #                     e_max = SAND_FINE_VOIDRATIO_MAX)

    # robot = robotModel(radius=15,AR=1,profile="VonKaraman", body_length=200)
    # sim1 = fineSand.getInterraction(robot,200)
    # sim1['z'] = sim1['depth']
    # sim1['med'] = sim1['force_z']
    # sim1['med'] = getFrictionFromSimulation(sim1,expAR1)
    # simAR1 = getWork(sim1)
    
    # z_index_sim = simAR1[simAR1['z'] < myDepth].index[-1]

    # energyFriction = np.array([simAR1['W_med'].iloc[z_index_sim],
    #                             simAR1['W_med'].iloc[z_index_sim]])   


    x_pos = [0,1]
    labels = ('$AR_1$','$AR_{1-Airflow}$')
    axs[1].bar(x_pos,energyFactors,color = colorArray,zorder=3,yerr=_err)
    # axs[1].bar(x_pos,PRESSURE_WORK_VEC,
    #     bottom=(energyFactors-PRESSURE_WORK_VEC),color="blue",zorder=4,yerr=_err)
    # #plt.title("Mechanical work required to reach 200mm depth")
    axs[1].grid(which="both",axis="y", linestyle='--')
    axs[1].set_ylabel('Energy [J]')
    axs[1].set_xticks(x_pos,['',''])
    axs[1].text(0.01, .87, 'B', fontsize=40,transform=axs[1].transAxes)
    
    plt.draw()
    
    plt.savefig("./results/Fig3_verticalAirflow.png", dpi=300)
    # plt.show()


    print("RAW data power values")
    outnames = ["AR1","AR1_AIR"]
    databloc = [expAR1,expAIR]

    for j,exp in enumerate(databloc):
        __arr = []
        for i in range(exp['N'][0]):
            __arr.append(exp['W_exp_'+str(i)].iloc[z_index])
            # print(exp['z_exp_'+str(i)].iloc[-1])
        print(outnames[j])
        print(__arr)


#pvalue 0.6578573459461617
print(PRESSURE_WORK_VEC)
