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

from bar_annotation import*
from expData.verticalExperiments import*
from expData.horizontalExperiments import*

if (__name__ == "__main__"):

    matplotlib.rc('font', **font)
    fig,axs = plt.subplots(2,1,figsize=(6,10)) #
    plt.subplots_adjust(left=.16,right=.95,top=0.85,bottom=0.05,hspace=0.35)


    #Plot AR1, AR1 Airflow
    axs[0].plot(expVACUUM_AR1_REF['z'],expVACUUM_AR1_REF['mean'],color=ColorList2[COLOR_H_AR1+2],label='$AR_1$')
    axs[0].fill_between(expVACUUM_AR1_REF['z'],expVACUUM_AR1_REF['m_std'], expVACUUM_AR1_REF['p_std'], color=ColorList2[COLOR_H_AR1+2], alpha=0.3)

    axs[0].plot(expVACUUM_AR1['z'],expVACUUM_AR1['mean'],color=ColorList[COLOR_VAC],label='$AR_1$ Vacuum 1mm/s 8g/s')
    axs[0].fill_between(expVACUUM_AR1['z'],expVACUUM_AR1['m_std'], expVACUUM_AR1['p_std'], color=ColorList[COLOR_VAC], alpha=0.3)
 
    leg = axs[0].legend(loc='upper center',draggable=True,ncol= 1,borderaxespad=0,bbox_to_anchor=(0, 1.3, 1., .102)) 
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    axs[0].grid(which="both")
    axs[0].set_ylabel('Force [N]')
    axs[0].set_xlabel('Depth [mm]')
    # axs[0].minorticks_on()
    axs[0].text(0.01, .87, 'A', fontsize=40,transform=axs[0].transAxes)
    plt.draw()

    #Energy estimation: [AR1, AR2.5, AR4, AIR, VACUUM]
    expAR1 = getWork(expAR1)
    expVACUUM_AR1_REF = getWork(expVACUUM_AR1_REF)
    expVACUUM_AR1 = getWork(expVACUUM_AR1)

    myDepth = 200
    z_index_VAC = expVACUUM_AR1[expVACUUM_AR1['z'] < myDepth].index[-1]
    z_index_REF = expVACUUM_AR1_REF[expVACUUM_AR1_REF['z'] < myDepth].index[-1]

    sand_density = 1.42e3 #[kg/m^3]
    robot_length = 200e-3
    R = 4e-3
    sand_volume = np.pi * R**2 * robot_length
    sand_mass = sand_volume * sand_density
    sand_flow = 8e-3 #[kg/s]
    advance_rate = 1e-3 #[m/s]
    sand_displaced = (myDepth*1e-3)/advance_rate * sand_flow   #[kg]

    dvolume_proportion = sand_displaced / sand_mass #proportion of volume moved inside the robot
    dvolume_distance = dvolume_proportion * robot_length #[m]
    
    print(dvolume_distance)

    #work at 200mm depth
    VACUUM_massWork = G_CONSTANT* sand_displaced *dvolume_distance #[mass work * distance]
    VACUUM_massWork_vec = np.array([0, VACUUM_massWork])
    

    energyFactors = np.array([
        expVACUUM_AR1_REF['W_mean'].iloc[z_index_REF], 
        expVACUUM_AR1['W_mean'].iloc[z_index_VAC], 
    ])
    print(VACUUM_massWork_vec)

    colorArray = [
        ColorList2[COLOR_H_AR1+2],
        ColorList[COLOR_VAC],
    ]

    _err = np.array([
        expVACUUM_AR1_REF['W_std'].iloc[z_index_REF],
        expVACUUM_AR1['W_std'].iloc[z_index_VAC], 
    ])

    
    x_pos = [0,1]
    labels = ('$AR_1$','$AR_{1-Vacuum}$')
    axs[1].bar(x_pos,energyFactors,color = colorArray,zorder=3)
    #axs[1].bar(x_pos,VACUUM_massWork_vec,bottom=energyFactors-VACUUM_massWork_vec,yerr=_err,color = "#0A3578",zorder=4)
    bar_add_annotation(axs[1],[0,1],15,0.014782227276510938,
                       alpha=0.6,dh=0.01,barh=0.01, barl=0.01,
                       fontfamily='Calibri', fontsize=20)
    # axs[1].bar(x_pos,energyFriction,bottom=(energyFactors-energyFriction),color="gray")
    # #plt.title("Mechanical work required to reach 200mm depth")
    axs[1].grid(which="both",axis="y", linestyle='--')
    axs[1].set_ylabel('Energy [J]')
    axs[1].set_xticks(x_pos,['',''])
    axs[1].text(0.01, .87, 'B', fontsize=40,transform=axs[1].transAxes)
    
    plt.draw()
    
    plt.savefig("./results/Fig4_verticalVacuum.png", dpi=300)
    # plt.show()

    print("EnergyFactors for each experiment")
    outnames = ["AR1","VACUUM"]
    indexes = [z_index_REF,z_index_VAC]
    for j,exp in enumerate([expVACUUM_AR1_REF,expVACUUM_AR1]):
        __arr = []
        for i in range(exp['N'][0]):
            __arr.append(exp['W_exp_'+str(i)].iloc[indexes[j]])
            # print(exp['z_exp_'+str(i)].iloc[-1])
        print(outnames[j])
        print(__arr)


    #pvalue 0.018417113193911604
