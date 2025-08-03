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
    fig,axs = plt.subplots(1,1,figsize=(6,5)) #
    plt.subplots_adjust(left=.16,right=.95,top=0.75,bottom=0.14,hspace=0.35)

    z_lim_fine = expAR1[expAR1['z'] <= 200].index
    z_lim_coarse = expVACUUM_AR1_REF[expVACUUM_AR1_REF['z'] <= 200].index


    #Plot AR1, AR1 Airflow
    axs.plot(expVACUUM_AR1_REF['z'].iloc[z_lim_coarse],expVACUUM_AR1_REF['mean'].iloc[z_lim_coarse],color=ColorList2[COLOR_H_AR1_ASYM1],label='$AR_1$ coarse')
    axs.fill_between(expVACUUM_AR1_REF['z'].iloc[z_lim_coarse],expVACUUM_AR1_REF['m_std'].iloc[z_lim_coarse], expVACUUM_AR1_REF['p_std'].iloc[z_lim_coarse], color=ColorList2[COLOR_H_AR1_ASYM1], alpha=0.3)

    axs.plot(expAR1['z'].iloc[z_lim_fine],expAR1['mean'].iloc[z_lim_fine],color=ColorList2[COLOR_H_AR1+1],label='$AR_1$ fine')
    axs.fill_between(expAR1['z'].iloc[z_lim_fine],expAR1['m_std'].iloc[z_lim_fine], expAR1['p_std'].iloc[z_lim_fine], color=ColorList2[COLOR_H_AR1+1], alpha=0.3)

    axs.plot(expAR25['z'].iloc[z_lim_fine],expAR25['mean'].iloc[z_lim_fine],color=ColorList2[COLOR_H_AR1+2],label='$AR_{25} fine$')
    axs.fill_between(expAR25['z'].iloc[z_lim_fine],expAR25['m_std'].iloc[z_lim_fine], expAR25['p_std'].iloc[z_lim_fine], color=ColorList2[COLOR_H_AR1+2], alpha=0.3)
    
    leg = axs.legend(loc='upper center',draggable=True,ncol= 2,borderaxespad=0,bbox_to_anchor=(0, 1.3, 1., .102)) 
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    axs.grid(which="both")
    axs.set_ylabel('Force [N]')
    axs.set_xlabel('Depth [mm]')
    # axs.minorticks_on()
    # axs.text(0.01, .87, 'A', fontsize=40,transform=axs.transAxes)
    plt.draw()

    #adapt to the same depth-sampling rate
    interpolator = interp1d(expVACUUM_AR1_REF['z'].iloc[z_lim_coarse], expVACUUM_AR1_REF['mean'].iloc[z_lim_coarse], axis=0, kind='linear', fill_value='extrapolate')
    interpolated_values = interpolator(expAR1['z'].iloc[z_lim_fine])
    coarse_err = np.mean(np.abs(expAR1['mean'].iloc[z_lim_fine] - interpolated_values))
    fine_err = np.mean(np.abs(expAR1['mean'].iloc[z_lim_fine] - expAR25['mean'].iloc[z_lim_fine]))
    print(coarse_err)
    print(fine_err)

    plt.savefig("./results/Fig5_compare_sands.png", dpi=300)
    plt.show()
    exit()

    #Energy estimation: [AR1, AR2.5, AR4, AIR, VACUUM]
    expAR1 = getWork(expAR1)
    expVACUUM_AR1_REF = getWork(expVACUUM_AR1_REF)

    VACUUM_time = 40
    VACUUM_mass = 8*VACUUM_time*1e-3 #kg of sand moved
    VACUUM_massWork = G_CONSTANT*VACUUM_mass*200e-3
    VACUUM_massWork_vec = np.array([0, VACUUM_massWork])
    expVACUUM_AR1 = getWork(expVACUUM_AR1, offset = VACUUM_massWork)
    
    myDepth = 200
    z_index_VAC = expVACUUM_AR1[expVACUUM_AR1['z'] < myDepth].index[-1]
    z_index_REF = expVACUUM_AR1_REF[expVACUUM_AR1_REF['z'] < myDepth].index[-1]

    energyFactors = np.array([
        expVACUUM_AR1_REF['W_mean'].iloc[z_index_REF], 
        expVACUUM_AR1['W_mean'].iloc[z_index_VAC], 
    ])

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
    axs[1].bar(x_pos,energyFactors,color = colorArray,yerr=_err,zorder=3)
    axs[1].bar(x_pos,VACUUM_massWork_vec,bottom=energyFactors-VACUUM_massWork_vec,color = "#0A3578",zorder=4)
    bar_add_annotation(axs[1],[0,1],20,0.018417113193911604,
                       alpha=0.6,dh=0.01,barh=0.01, barl=0.01,
                       fontfamily='Calibri', fontsize=20)
    # axs[1].bar(x_pos,energyFriction,bottom=(energyFactors-energyFriction),color="gray")
    # #plt.title("Mechanical work required to reach 200mm depth")
    axs[1].grid(which="both",axis="y", linestyle='--')
    axs[1].set_ylabel('Energy [J]')
    axs[1].set_xticks(x_pos,['',''])
    axs[1].text(0.01, .87, 'B', fontsize=40,transform=axs[1].transAxes)
    
    plt.draw()
    
    #plt.savefig("./results/Fig4_verticalVacuum.png", dpi=300)
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
