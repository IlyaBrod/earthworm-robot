# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

#Figure1 A: AR1,AR2.5,AR4 vertical 
#        B: Energy AR1, AR2.5, AR4
#        C: Table values of 3 points
from CONFIG import*
from RobotModel import*
from SoilModel import*
from expData.processFunctions import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from bar_annotation import *
from expData.verticalExperiments import*
from expData.horizontalExperiments import*

if (__name__ == "__main__"):

    matplotlib.rc('font', **font)
    fig,axs = plt.subplots(2,1,figsize=(6,10)) #
    # fig.add_gridspec(hspace=0,wspace=0.2)
    plt.subplots_adjust(left=.16,right=.95,top=0.85,bottom=0.05,hspace=0.35) #,wspace=0.3
    #plt.tight_layout()
    #Plot AR1, AR2.5, AR4
    
    axs[0].plot(expAR1['z'],expAR1['mean'],color=ColorList2[COLOR_H_AR1+2],label='$AR_1$',zorder=2)
    axs[0].fill_between(expAR1['z'],expAR1['m_std'], expAR1['p_std'], color=ColorList2[COLOR_H_AR1+1], alpha=0.3,zorder=2)
    # # # #1.12

    axs[0].plot(expAR1_ASYM['z'],expAR1_ASYM['mean'],color=ColorList2[COLOR_H_AR1_ASYM1],label='$AR_{1A}$',zorder=2)
    axs[0].fill_between(expAR1_ASYM['z'],expAR1_ASYM['m_std'], expAR1_ASYM['p_std'], color=ColorList2[COLOR_H_AR1_ASYM1], alpha=0.3,zorder=2)

    axs[0].plot(expAR25['z'],expAR25['mean'],color=ColorList2[COLOR_H_AR25+2],label='$AR_{2.5}$',zorder=2)
    axs[0].fill_between(expAR25['z'],expAR25['m_std'], expAR25['p_std'], color=ColorList2[COLOR_H_AR25+1], alpha=0.3,zorder=2)

    axs[0].plot(expAR4['z'][expAR4['z'] <= expAR1['z'].iloc[-1]],expAR4['mean'][expAR4['z'] <= expAR1['z'].iloc[-1]],color=ColorList2[COLOR_H_AR4+2],label='$AR_4$',zorder=2)
    axs[0].fill_between(expAR4['z'][expAR4['z'] <= expAR1['z'].iloc[-1]],expAR4['m_std'][expAR4['z'] <= expAR1['z'].iloc[-1]], expAR4['p_std'][expAR4['z'] <= expAR1['z'].iloc[-1]], color=ColorList2[COLOR_H_AR4+1], alpha=0.3,zorder=2)

    leg = axs[0].legend(loc='upper center',draggable=True,ncol= 2,borderaxespad=0,bbox_to_anchor=(0, 1.3, 1., .102)) 
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    
    axs[0].set_ylabel('Force [N]')
    axs[0].set_xlabel('Depth [mm]')
    # axs[0].minorticks_on()
    axs[0].text(0.01, .87, 'A', fontsize=40,transform=axs[0].transAxes)
    axs[0].grid(which="both",zorder=1)
    plt.draw()

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

    #resample AR4 data
    expAR4_rs = dict()
    expAR4_rs['mean'] = synch_rates(expAR4['mean'],expAR4['z'],expAR1['z'])
    expAR4_rs['z'] = expAR1['z'].values
    expAR4_rs = pd.DataFrame(expAR4_rs)


    # plt.figure(figsize=(10,6))
    #Energy estimation: [AR1, AR2.5, AR4, AIR, VACUUM]
    expAR1 = getWork(expAR1)
    expAR25 = getWork(expAR25)
    expAR4 = getWork(expAR4)
    expAR1_ASYM = getWork(expAR1_ASYM)


    #get friction proportion
    
    fineSand = SoilModel("fine sand",
                         bulk_density=SAND_FINE_BULK_DENSITY[SELECT_DENSITY],
                         particle_density = SAND_FINE_GRAIN_DENSITY,
                         interface_friction = SAND_FINE_INTERFACE_FRICTION,
                         friction = SAND_FINE_FRICTION,
                         tank_H = TANK_HEIGHT,
                         tank_D = TANK_DIAMETER,
                         e_min = SAND_FINE_VOIDRATIO_MIN,
                         e_max = SAND_FINE_VOIDRATIO_MAX)

    robot = robotModel(radius=15,AR=1,profile="VonKaraman", body_length=200)
    sim1 = fineSand.getInterraction(robot,200)
    sim1['z'] = sim1['depth']
    sim1['med'] = getFrictionFromSimulation(sim1,expAR1)
    simAR1 = getWork(sim1)

    robot = robotModel(radius=15,AR=2.5,profile="VonKaraman", body_length=200)
    sim1 = fineSand.getInterraction(robot,200)
    sim1['z'] = sim1['depth']
    sim1['med'] = getFrictionFromSimulation(sim1,expAR25)
    simAR25 = getWork(sim1)

    robot = robotModel(radius=15,AR=4,profile="VonKaraman", body_length=200)
    sim1 = fineSand.getInterraction(robot,200)
    sim1['z'] = sim1['depth']
    sim1['med'] = getFrictionFromSimulation(sim1,expAR4)
    simAR4 = getWork(sim1)

    # print(simAR4)

    #Building the arrays to plot
    #Mechanical work at the last depth
    z_index_AR1 = expAR1[expAR1['z'] < 200].index[-1]
    z_index_AR25 = expAR1[expAR1['z'] < 200].index[-1]
    z_index_AR4 = expAR4[expAR4['z'] < 200].index[-1]
    
    z_index_sim_AR1 = simAR1[simAR1['z'] < 200].index[-1]
    z_index_sim_AR25 = simAR25[simAR25['z'] < 200].index[-1]
    z_index_sim_AR4 = simAR4[simAR4['z'] < 200].index[-1]

    
    energyFactors = np.array([
        expAR1_ASYM['W_mean'].iloc[z_index_AR1], 
        expAR1['W_mean'].iloc[z_index_AR1], 
        expAR25['W_mean'].iloc[z_index_AR25], 
        expAR4['W_med'].iloc[z_index_AR4]
    ])

    print("Compare energy values: ")
    print((energyFactors[1]-energyFactors[3])/energyFactors[1] * 100)


    energyFriction = np.array([simAR1['W_med'].iloc[z_index_sim_AR1],
                                simAR1['W_med'].iloc[z_index_sim_AR1],
                                simAR25['W_med'].iloc[z_index_sim_AR25],
                                simAR4['W_med'].iloc[z_index_sim_AR4]])                                                

    print(energyFriction)
    
    _err = [
        expAR1_ASYM['W_std'].iloc[z_index_AR1], 
        expAR1['W_std'].iloc[z_index_AR1],  
        expAR25['W_std'].iloc[z_index_AR25], 
        expAR4['W_std'].iloc[z_index_AR4]
    ]

    colorPicker = [
        ColorList2[COLOR_H_AR1_ASYM1],
        ColorList2[COLOR_H_AR1+2],
        ColorList2[COLOR_H_AR25+2],
        ColorList2[COLOR_H_AR4+2]
    ]

    pvalues = [0.03330004605113471, 0.008592803303155155, 0.0015366260089722042]

    x_pos = [0,1,2,3]
    labels = ('$AR_1$','$AR_{2.5}$','$AR_4$')
    axs[1].grid(which="both",axis="y", linestyle='--',zorder=1)
    axs[1].bar(x_pos,energyFactors,color = colorPicker,zorder=2)
    axs[1].bar(x_pos,energyFriction,bottom=(energyFactors-energyFriction),color="gray",zorder=3,yerr=_err)
    # #plt.title("Mechanical work required to reach 200mm depth")
    axs[1].set_ylabel('Energy [J]')
    axs[1].set_xticks(x_pos,['','','',''])
    axs[1].text(0.01, .87, 'B', fontsize=40,transform=axs[1].transAxes)
    
    bar_add_annotation(axs[1],[0,1],11,pvalues[0],
                       alpha=0.6,dh=0.01,barh=0.01, barl=0.01,hspace = 0.01,
                       fontfamily='Calibri', fontsize=20)
    bar_add_annotation(axs[1],[2,1],10,pvalues[1],
                       alpha=0.6,dh=0.01,barh=0.01, barl=0.01,hspace = 0.01,
                       fontfamily='Calibri', fontsize=20)
    bar_add_annotation(axs[1],[3,1],11,pvalues[2],
                       alpha=0.6,dh=0.01,barh=0.01, barl=0.01,hspace = 0.01,
                       fontfamily='Calibri', fontsize=20)

    plt.draw()

    # plt.savefig("./results/Fig1_vertical.png", dpi=300)
    
    # plt.show()
    
    print("energyFactors:")
    outnames = ["AR1","AR1_ASYM","AR25","AR4"]
    indexList = [z_index_AR1,z_index_AR1,z_index_AR25,z_index_AR4]
    for j,exp in enumerate([expAR1,expAR1_ASYM,expAR25,expAR4]):
        __arr = []
        for i in range(exp['N'][0]):
            __arr.append(exp['W_exp_'+str(i)][indexList[j]])
            # print(exp['z_exp_'+str(i)].iloc[-1])
        print(outnames[j])
        print(__arr)



