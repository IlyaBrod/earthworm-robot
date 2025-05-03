# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

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

    # plt.figure()
    # #Plot AR1, AR2.5, AR4
    # plt.plot(expAR1_depth,expAR1_med,color=ColorList[1],label='Experimental med. $AR_1$')
    # plt.fill_between(expAR1_depth,expAR1_min, expAR1_max, color=ColorList[1], alpha=0.3)
    # # # #1.12

    # # # plt.plot(expAR1_ASYM_depth,expAR1_ASYM_med,color=ColorList2[2],label='Experimental med. $AR_{1A}$')
    # # # plt.fill_between(expAR1_ASYM_depth,expAR1_ASYM_min, expAR1_ASYM_max, color=ColorList2[2], alpha=0.3)

    # plt.plot(expAR25_depth,expAR25_med,color=ColorList[3],label='Experimental med. $AR_{2.5}$')
    # plt.fill_between(expAR25_depth,expAR25_min, expAR25_max, color=ColorList[3], alpha=0.3)

    # plt.plot(expAR4_depth,expAR4_med,color=ColorList[4],label='Experimental med. $AR_4$')
    # plt.fill_between(expAR4_depth,expAR4_min, expAR4_max, color=ColorList[4], alpha=0.3)

    # plt.legend(loc='upper left')
    # # plt.title("Vertical penetration force $F_z$")
    # plt.grid(which="both")
    # plt.ylabel('Force [N]')
    # plt.xlabel('Depth Z [mm]')
    # plt.draw()

    # arr = expAR1_med[expAR1_depth>125]
    # drr = expAR1_depth[expAR1_depth>125]
    # m,b = np.polyfit(np.concatenate((drr,drr,drr)),np.concatenate((arr,arr,arr)),1)
    # print(m,b)

    # #0.7 for AR4
    # #1.1 for AR1
    # #0.8 for AR2.5
    # slope = m #np.tan(45*np.pi/180)
    # x = np.linspace(125, 225, 100)
    # y = slope * x + b
    # plt.plot(x, y)

    

    # plt.savefig("./results/CompareAR.png", dpi=300)

    # plt.figure()
    # #Plot AR1, AIR, VACUUM
    # #Plot AR1, AR2.5, AR4
    # plt.plot(expAR1['z'],expAR1['med'],color=ColorList[1],label='Experimental med. $AR_1$')
    # plt.fill_between(expAR1['z'],expAR1['min'], expAR1['max'], color=ColorList[1], alpha=0.3)

    # # plt.plot(expAIR_depth,expAIR_med,color=ColorList[0],label='Experimental med. Airflow 34kPa')
    # # plt.fill_between(expAIR_depth,expAIR_min, expAIR_max, color=ColorList[0], alpha=0.3)

    # plt.plot(expVACUUM_AR1['z'],expVACUUM_AR1['med'],color=ColorList[2],label='Experimental med. Vacuum 1mm/s 8g/s')
    # plt.fill_between(expVACUUM_AR1['z'],expVACUUM_AR1['min'], expVACUUM_AR1['max'], color=ColorList[2], alpha=0.3)
 
    # plt.plot(expVACUUM_AR1_REF['z'],expVACUUM_AR1_REF['med'],color=ColorList[5],label='Experimental med. 5mm/s AR_1')
    # plt.fill_between(expVACUUM_AR1_REF['z'],expVACUUM_AR1_REF['min'], expVACUUM_AR1_REF['max'], color=ColorList[5], alpha=0.3)

    # plt.plot(expAR1_depth,expAR1_med,color=ColorList[1],label='Experimental med. AR1')
    # plt.fill_between(expAR1_depth,expAR1_min, expAR1_max, color=ColorList[1], alpha=0.3)

    #plt.plot(expVACUUM_AR25_depth,expVACUUM_AR25_med,color=ColorList[5],label='Experimental med. Vacuum 5mm/s')
    #plt.fill_between(expVACUUM_AR25_depth,expVACUUM_AR25_min, expVACUUM_AR25_max, color=ColorList[5], alpha=0.3)

    # plt.legend()
    # # plt.title("Vertical penetration force $F_z$")
    # plt.grid(which="both")
    # plt.ylabel('Force [N]')
    # plt.xlabel('Depth Z [mm]')
    # plt.draw()
    # plt.savefig("./results/CompareActive.png", dpi=300)

    # plt.figure(figsize=(10,6))
    # plt.plot(expAR1_depth_H120,expAR1_med_H120,color=ColorList2[0],label='$AR_1$ Z=120mm',linewidth=2)
    # plt.fill_between(expAR1_depth_H120,expAR1_min_H120, expAR1_max_H120, color=ColorList2[0], alpha=0.2)

    # plt.plot(expAR1_ASYM0_depth_H120,expAR1_ASYM0_med_H120,color=ColorList2[9],label='$AR_{1A-UP}$ Z=120mm',linewidth=2)
    # plt.fill_between(expAR1_ASYM0_depth_H120,expAR1_ASYM0_min_H120, expAR1_ASYM0_max_H120, color=ColorList2[9], alpha=0.2)

    # plt.plot(expAR1_ASYM1_depth_H120,expAR1_ASYM1_med_H120,color=ColorList2[12],label='$AR_{1A-DOWN}$ Z=120mm',linewidth=2)
    # plt.fill_between(expAR1_ASYM1_depth_H120,expAR1_ASYM1_min_H120, expAR1_ASYM1_max_H120, color=ColorList2[12], alpha=0.2)

    # plt.plot(expAR1_depth_H220,expAR1_med_H220,color=ColorList2[1],label='$AR_1$ Z=220mm',linewidth=2)
    # # plt.fill_between(expAR1_depth_H220,expAR1_min_H220, expAR1_max_H220, color=ColorList2[3], alpha=0.3)

    # plt.plot(expAR1_depth_H320,expAR1_med_H320,color=ColorList2[2],label='$AR_1$ Z=320mm',linewidth=2)
    # # plt.fill_between(expAR1_depth_H320,expAR1_min_H320, expAR1_max_H320, color=ColorList2[3], alpha=0.3)


    # plt.plot(expAR25_depth_H120,expAR25_med_H120,color=ColorList2[3],label='$AR_{2.5}$ Z=120mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H120,expAR25_min_H120, expAR25_max_H120, color=ColorList2[2], alpha=0.3)

    # plt.plot(expAR25_depth_H220,expAR25_med_H220,color=ColorList2[4],label='$AR_{2.5}$ Z=220mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H220,expAR25_min_H220, expAR25_max_H220, color=ColorList2[2], alpha=0.3)

    # plt.plot(expAR25_depth_H320,expAR25_med_H320,color=ColorList2[5],label='$AR_{2.5}$ Z=320mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H320,expAR25_min_H320, expAR25_max_H320, color=ColorList2[2], alpha=0.3)


    # plt.plot(expAR4_depth_H120,expAR4_med_H120,color=ColorList2[6],label='$AR_4$ Z=120mm',linewidth=2)
    # # plt.fill_between(expAR4_depth_H120,expAR4_min_H120, expAR4_max_H120, color=ColorList2[1], alpha=0.3)

    # plt.plot(expAR4_depth_H220,expAR4_med_H220,color=ColorList2[7],label='$AR_4$ Z=220mm',linewidth=2)
    # # plt.fill_between(expAR4_depth_H220,expAR4_min_H220, expAR4_max_H220, color=ColorList2[1], alpha=0.3)

    # plt.plot(expAR4_depth_H320,expAR4_med_H320,color=ColorList2[8],label='$AR_4$ Z=320mm',linewidth=2.0)
    # # plt.fill_between(expAR4_depth_H320,expAR4_min_H320, expAR4_max_H320, color=ColorList2[1], alpha=0.3)

    # plt.legend(loc='lower right', fontsize='large')
    # # plt.title("Horizontal penetration force $F_z$")
    # plt.grid(which="both")
    # plt.ylabel('Force [N]')
    # plt.xlabel('Distance X [mm]')
    # plt.draw()
    # plt.savefig("./results/CompareHorizontal_ASYM.png", dpi=300)

    #plt.figure()
    #Energy estimation: [AR1, AR2.5, AR4, AIR, VACUUM]
    expAR1 = getWork(expAR1)
    expAR1_H120 = getWork(expAR1_H120,depth=97.50)
    expAR1_H220 = getWork(expAR1_H220,depth=97.50)
    expAR1_H320 = getWork(expAR1_H320,depth=97.50)
    expAR1_ASYM = getWork(expAR1_ASYM)
    expAR1_ASYM0_H120 = getWork(expAR1_ASYM0_H120,depth=97.50)
    expAR1_ASYM = getWork(expAR1_ASYM)
    expAR1_ASYM1_H120 = getWork(expAR1_ASYM1_H120,depth=97.50)
    expAR25 = getWork(expAR25)
    expAR25_H120 = getWork(expAR25_H120,depth=97.50)
    expAR25_H220 = getWork(expAR25_H220,depth=97.50)
    expAR25_H320 = getWork(expAR25_H320,depth=97.50)
    expAR4 = getWork(expAR4)
    expAR4_H120 = getWork(expAR4_H120,depth=97.50)
    expAR4_H220 = getWork(expAR4_H220,depth=97.50)
    expAR4_H320 = getWork(expAR4_H320,depth=97.50)

    # #Air blowing system 34kPa "constant" pressure 3mm hole diameter
    AIR_surface = np.pi * (1.5e-3)**2
    expAIR = getWork(expAIR)
    expAIR['W_med'] += (34e3 * AIR_surface * 200e-3)
    expAIR['W_min'] += (34e3 * AIR_surface * 200e-3)
    expAIR['W_max'] += (34e3 * AIR_surface * 200e-3)

    VACUUM_time = 40
    VACUUM_mass = 8*VACUUM_time*1e-3 #kg of sand moved
    VACUUM_massWork = G_CONSTANT*VACUUM_mass*200e-3
    expVACUUM_AR1 = getWork(expVACUUM_AR1)
    expVACUUM_AR1['W_med'] += VACUUM_massWork
    expVACUUM_AR1['W_max'] += VACUUM_massWork
    expVACUUM_AR1['W_min'] += VACUUM_massWork
    
    energyFactors = np.array([
        expAIR['W_med'][0], 
        expAR1['W_med'][0], 
        expVACUUM_AR1['W_med'][0], 
        expAR25['W_med'][0], 
        expAR4['W_med'][0]
    ])

    _errMin = [
        expAIR['W_med'][0] - expAIR['W_min'][0], 
        expAR1['W_med'][0] - expAR1['W_min'][0], 
        expVACUUM_AR1['W_med'][0] - expVACUUM_AR1['W_min'][0], 
        expAR25['W_med'][0] - expAR25['W_min'][0], 
        expAR4['W_med'][0] - expAR4['W_min'][0]
    ]

    _errMax = [
        expAIR['W_max'][0] - expAIR['W_med'][0], 
        expAR1['W_max'][0] - expAR1['W_med'][0], 
        expVACUUM_AR1['W_max'][0] - expVACUUM_AR1['W_med'][0], 
        expAR25['W_max'][0] - expAR25['W_med'][0], 
        expAR4['W_max'][0] - expAR4['W_med'][0]
    ]

    # x_pos = [0,1,2,4,5]
    # labels = ('Airflow','$AR_1$','Vacuum','$AR_{2.5}$','$AR_4$')
    # plt.bar(x_pos,energyFactors,color = ColorList,yerr=[_errMin,_errMax],capsize=10)
    # #plt.title("Mechanical work required to reach 200mm depth")
    # plt.grid(which="both",axis="y")
    # plt.ylabel('Energy [J]')
    # plt.xticks(x_pos,labels)
    # plt.savefig("./results/EnergyRequirements_vertical_split.png", dpi=300)
    # plt.draw()


    #Plot using the reference AR1, d=1.42g/cm^3
    #coefficient = (W_AR1 - W_X)/ W_AR1 x 100
    REF_VAL = expAR1['W_med'][0]
    #print(expAR1_ASYM1_H120['W_med'][0],expAR1_ASYM0_H120['W_med'][0],expAR1_H120['W_med'][0])
    fullFactor = np.array([
        expAR1_H120['W_med'][0], 
        expAR1_ASYM0_H120['W_med'][0], 
        expAR1_ASYM1_H120['W_med'][0], 
        # expAR1_H220['W_med'][0], 
        # expAR1_H320['W_med'][0], 
        # expAR25_H120['W_med'][0], 
        # expAR25_H220['W_med'][0], 
        # expAR25_H320['W_med'][0], 
        # expAR4_H120['W_med'][0], 
        # expAR4_H220['W_med'][0], 
        # expAR4_H320['W_med'][0], 
        #getRFactor(expAIR['W_med'][0],REF_VAL), 
        #getRFactor(expAR1['W_med'][0],REF_VAL), 
        #getRFactor(expAR1_ASYM['W_med'][0],REF_VAL)
        #getRFactor(expVACUUM_AR1['W_med'][0],REF_VAL),
        #getRFactor(expAR25['W_med'][0],REF_VAL), 
        #getRFactor(expAR4['W_med'][0],REF_VAL)
    ])

    colorArray = [
        ColorList2[COLOR_H_AR1],
        ColorList2[COLOR_H_AR1_ASYM0],
        ColorList2[COLOR_H_AR1_ASYM1],
        # ColorList2[COLOR_H_AR1+1],
        # ColorList2[COLOR_H_AR1+2],
        # ColorList2[COLOR_H_AR25],
        # ColorList2[COLOR_H_AR25+1],
        # ColorList2[COLOR_H_AR25+2],
        # ColorList2[COLOR_H_AR4],
        # ColorList2[COLOR_H_AR4+1],
        # ColorList2[COLOR_H_AR4+2],
        #ColorList[COLOR_AR1],
        #ColorList[COLOR_AR1_ASYM]
        #ColorList[COLOR_AR25],
        #ColorList[COLOR_AR4]
    ]

    _errMin = np.array([
        expAR1_H120['W_med'][0]-expAR1_H120['W_min'][0], 
        # expAR1_H220['W_med'][0]-expAR1_H220['W_min'][0], 
        # expAR1_H320['W_med'][0]-expAR1_H320['W_min'][0], 
        
        expAR1_ASYM0_H120['W_med'][0]-expAR1_ASYM0_H120['W_min'][0],
        expAR1_ASYM1_H120['W_med'][0]-expAR1_ASYM1_H120['W_min'][0],

        # expAR25_H120['W_med'][0]-expAR25_H120['W_min'][0], 
        # expAR25_H220['W_med'][0]-expAR25_H220['W_min'][0], 
        # expAR25_H320['W_med'][0]-expAR25_H320['W_min'][0],         
        
        # expAR4_H120['W_med'][0]-expAR4_H120['W_min'][0], 
        # expAR4_H220['W_med'][0]-expAR4_H220['W_min'][0], 
        # expAR4_H320['W_med'][0]-expAR4_H320['W_min'][0], 

        #expAIR['W_med'][0] - expAIR['W_min'][0], 
        #getRFactor(expAR1['W_med'][0],REF_VAL) - getRFactor(expAR1['W_min'][0],REF_VAL), 
        #getRFactor(expAR1_ASYM['W_med'][0],REF_VAL) - getRFactor(expAR1_ASYM['W_min'][0],REF_VAL) 
        #expVACUUM_AR1['W_med'][0] - expVACUUM_AR1['W_min'][0], 
        #getRFactor(expAR25['W_med'][0],REF_VAL) - getRFactor(expAR25['W_min'][0],REF_VAL), 
        #getRFactor(expAR4['W_med'][0],REF_VAL) - getRFactor(expAR4['W_min'][0],REF_VAL)
    ])

    _errMax = np.array([
        expAR1_H120['W_max'][0]-expAR1_H120['W_med'][0], 
        # expAR1_H220['W_max'][0]-expAR1_H220['W_med'][0], 
        # expAR1_H320['W_max'][0]-expAR1_H320['W_med'][0], 
        
        expAR1_ASYM0_H120['W_max'][0]-expAR1_ASYM0_H120['W_med'][0],
        expAR1_ASYM1_H120['W_max'][0]- expAR1_ASYM1_H120['W_med'][0],

        # expAR25_H120['W_max'][0]-expAR25_H120['W_med'][0], 
        # expAR25_H220['W_max'][0]-expAR25_H220['W_med'][0], 
        # expAR25_H320['W_max'][0]-expAR25_H320['W_med'][0], 
        
        # expAR4_H120['W_max'][0]-expAR4_H120['W_med'][0], 
        # expAR4_H220['W_max'][0]-expAR4_H220['W_med'][0], 
        # expAR4_H320['W_max'][0]-expAR4_H320['W_med'][0], 

        #expAIR['W_max'][0] - expAIR['W_med'][0], 
        #getRFactor(expAR1['W_max'][0],REF_VAL) - getRFactor(expAR1['W_med'][0],REF_VAL), 
        #getRFactor(expAR1_ASYM['W_max'][0],REF_VAL) - getRFactor(expAR1_ASYM['W_med'][0],REF_VAL) 
        #expVACUUM_AR1['W_max'][0] - expVACUUM_AR1['W_med'][0], 
        #getRFactor(expAR25['W_max'][0],REF_VAL) - getRFactor(expAR25['W_med'][0],REF_VAL), 
        #getRFactor(expAR4['W_max'][0],REF_VAL) - getRFactor(expAR4['W_med'][0],REF_VAL)
    ])

    print(fullFactor)
    
    print(_errMax)
    print(_errMin)

    matplotlib.rc('font', **font)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    x_pos = [0,1,2]
    # labels = ('$AR_{1-120}$','$AR_{1-220}$','$AR_{1-320}$',
    #           '$AR_{2.5-120}$','$AR_{2.5-220}$','$AR_{2.5-320}$',
    #           '$AR_{4-120}$','$AR_{4-220}$','$AR_{4-320}$')
    labels = ('$AR_{1-120}$','$AR_{1A-UP-120}$','$AR_{1A-DOWN-120}$')
    plt.bar(x_pos,fullFactor,color = colorArray,capsize=10,yerr=[_errMin,_errMax])
    # plt.plot(np.array([-0.4, .4]),[0,0], color=colorArray[0],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+1,[0,0], color=colorArray[1],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+2,[0,0], color=colorArray[2],linewidth=3)
    plt.ylabel('Energy [J]',labelpad=0)
    plt.xticks(x_pos,labels,rotation=45)
    #plt.minorticks_on()
    ax.grid(which='minor', axis='y', linestyle=':', color='gray', alpha=0.2, zorder=0)
    ax.grid(axis='y',zorder=0)
    plt.tight_layout()
    
    plt.draw()
    plt.savefig("./results/Plot4.png", dpi=300)
    
    plt.show()





