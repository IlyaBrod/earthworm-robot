# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.

# Figure2 : A Horizontal AR1, AR2.5, AR4
#           B Horizontal AR1, AR1 asym1, AR1 asym2
#           C Energy Horizontal AR1, AR2.5, AR4
#           D Energy Horizontal AR1, AR1 asym1, AR1 asym2

from CONFIG import*
from RobotModel import*
from SoilModel import*
from expData.processFunctions import *
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec

from bar_annotation import *
from expData.verticalExperiments import*
from expData.horizontalExperiments import*

if (__name__ == "__main__"):

    matplotlib.rc('font', **font)

    fig = plt.figure(figsize=(19, 14))

    # Définir une grille avec GridSpec (2x2)
    gs = GridSpec(2, 3, hspace=.2, wspace=0.2)
    plt.subplots_adjust(left=.05,right=.99,top=.89,bottom=0.05)

    # Ajouter les sous-tracés
    ax1 = fig.add_subplot(gs[0, :2])  # Fusionne les deux colonnes pour ce sous-tracé
    ax2 = fig.add_subplot(gs[:, 2])  # Sous-tracé en bas à gauche
    ax3 = fig.add_subplot(gs[1, 0])  # Sous-tracé en bas à droite
    ax4 = fig.add_subplot(gs[1, 1])  # Deuxième rangée, première colonne


    
    ax1.plot(expAR1_H120['z'],expAR1_H120['mean'],color=ColorList2[0],label='$AR_1$ z=120mm',linewidth=2)
    # plt.fill_between(expAR1_H120['z'],expAR1_H120['min'], expAR1_H120['max'], color=ColorList2[0], alpha=0.2)

    # plt.plot(expAR1_ASYM0_depth_H120,expAR1_ASYM0_med_H120,color=ColorList2[9],label='$AR_{1A-UP}$ Z=120mm',linewidth=2)
    # plt.fill_between(expAR1_ASYM0_depth_H120,expAR1_ASYM0_min_H120, expAR1_ASYM0_max_H120, color=ColorList2[9], alpha=0.2)

    # plt.plot(expAR1_ASYM1_depth_H120,expAR1_ASYM1_med_H120,color=ColorList2[12],label='$AR_{1A-DOWN}$ Z=120mm',linewidth=2)
    # plt.fill_between(expAR1_ASYM1_depth_H120,expAR1_ASYM1_min_H120, expAR1_ASYM1_max_H120, color=ColorList2[12], alpha=0.2)

    ax1.plot(expAR1_H220['z'],expAR1_H220['mean'],color=ColorList2[1],label='$AR_1$ z=220mm',linewidth=2)
    # ax1.fill_between(expAR1_depth_H220,expAR1_min_H220, expAR1_max_H220, color=ColorList2[3], alpha=0.3)

    ax1.plot(expAR1_H320['z'],expAR1_H320['mean'],color=ColorList2[2],label='$AR_1$ z=320mm',linewidth=2)
    # ax1.fill_between(expAR1_depth_H320,expAR1_min_H320, expAR1_max_H320, color=ColorList2[3], alpha=0.3)


    ax1.plot(expAR25_H120['z'],expAR25_H120['mean'],color=ColorList2[3],label='$AR_{2.5}$ z=120mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H120,expAR25_min_H120, expAR25_max_H120, color=ColorList2[2], alpha=0.3)

    ax1.plot(expAR25_H220['z'],expAR25_H220['mean'],color=ColorList2[4],label='$AR_{2.5}$ z=220mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H220,expAR25_min_H220, expAR25_max_H220, color=ColorList2[2], alpha=0.3)

    ax1.plot(expAR25_H320['z'],expAR25_H320['mean'],color=ColorList2[5],label='$AR_{2.5}$ z=320mm',linewidth=2)
    # # plt.fill_between(expAR25_depth_H320,expAR25_min_H320, expAR25_max_H320, color=ColorList2[2], alpha=0.3)


    ax1.plot(expAR4_H120['z'],expAR4_H120['mean'],color=ColorList2[6],label='$AR_4$ z=120mm',linewidth=2)
    # # plt.fill_between(expAR4_depth_H120,expAR4_min_H120, expAR4_max_H120, color=ColorList2[1], alpha=0.3)

    ax1.plot(expAR4_H220['z'],expAR4_H220['mean'],color=ColorList2[7],label='$AR_4$ z=220mm',linewidth=2)
    # # plt.fill_between(expAR4_depth_H220,expAR4_min_H220, expAR4_max_H220, color=ColorList2[1], alpha=0.3)

    ax1.plot(expAR4_H320['z'],expAR4_H320['mean'],color=ColorList2[8],label='$AR_4$ z=320mm',linewidth=2.0)
    # # plt.fill_between(expAR4_depth_H320,expAR4_min_H320, expAR4_max_H320, color=ColorList2[1], alpha=0.3)

    leg = ax1.legend(loc='lower right',mode="expand",ncol= 3,borderaxespad=0,bbox_to_anchor=(0.3, 1.02, 1., .102))
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    # # plt.title("Horizontal penetration force $F_z$")
    ax1.grid(which="both")
    ax1.set_ylabel('Force [N]')
    ax1.set_xlabel('Distance X [mm]')
    ax1.text(0.01, .87, 'A', fontsize=60,transform=ax1.transAxes)
    plt.draw()
    # plt.savefig("./results/CompareHorizontal_ASYM.png", dpi=300)

    ######ASYM
    ax3.plot(expAR1_H120['z'],expAR1_H120['mean'],color=ColorList2[0],label='$AR_1$',linewidth=2)
    ax3.fill_between(expAR1_H120['z'],expAR1_H120['m_std'], expAR1_H120['p_std'], color=ColorList2[0], alpha=0.4)

    ax3.plot(expAR1_ASYM0_H120['z'],expAR1_ASYM0_H120['mean'],color=ColorList2[9],label='$AR_{1A-UP}$',linewidth=2)
    ax3.fill_between(expAR1_ASYM0_H120['z'],expAR1_ASYM0_H120['m_std'], expAR1_ASYM0_H120['p_std'], color=ColorList2[9], alpha=0.4)

    ax3.plot(expAR1_ASYM1_H120['z'],expAR1_ASYM1_H120['mean'],color=ColorList2[12],label='$AR_{1A-DOWN}$',linewidth=2)
    ax3.fill_between(expAR1_ASYM1_H120['z'],expAR1_ASYM1_H120['m_std'], expAR1_ASYM1_H120['p_std'], color=ColorList2[12], alpha=0.4)

    leg = ax3.legend(loc='lower right',ncol= 1,borderaxespad=0)
    for legobj in leg.legend_handles:
        legobj.set_linewidth(10.0)
    # # plt.title("Horizontal penetration force $F_z$")
    ax3.grid(which="both")
    ax3.set_ylabel('Force [N]')
    ax3.set_xlabel('Distance X [mm]')
    ax3.text(0.01, .87, 'C', fontsize=60,transform=ax3.transAxes)
    plt.draw()

    ########ENERGY
    myDepth = 97.50
    #Energy estimation: [AR1, AR2.5, AR4, AIR, VACUUM]
    expAR1 = getWork(expAR1)
    expAR1_H120 = getWork(expAR1_H120)
    expAR1_H220 = getWork(expAR1_H220)
    expAR1_H320 = getWork(expAR1_H320)

    expAR1_ASYM = getWork(expAR1_ASYM)
    expAR1_ASYM0_H120 = getWork(expAR1_ASYM0_H120)
    expAR1_ASYM = getWork(expAR1_ASYM)
    expAR1_ASYM1_H120 = getWork(expAR1_ASYM1_H120)

    expAR25 = getWork(expAR25)
    expAR25_H120 = getWork(expAR25_H120)
    expAR25_H220 = getWork(expAR25_H220)
    expAR25_H320 = getWork(expAR25_H320)

    expAR4 = getWork(expAR4)
    expAR4_H120 = getWork(expAR4_H120)
    expAR4_H220 = getWork(expAR4_H220)
    expAR4_H320 = getWork(expAR4_H320)
    
    z_index = expAR1_H120[expAR1_H120['z'] < myDepth].index[-1]
             
    #Plot horizontal asymetric
    fullFactor = np.array([
        expAR1_H120['W_mean'].iloc[z_index],
        expAR25_H120['W_mean'].iloc[z_index],
        expAR4_H120['W_mean'].iloc[z_index],  

        expAR1_H220['W_mean'].iloc[z_index], 
        expAR25_H220['W_mean'].iloc[z_index], 
        expAR4_H220['W_mean'].iloc[z_index], 

        expAR1_H320['W_mean'].iloc[z_index], 
        expAR25_H320['W_mean'].iloc[z_index],
        expAR4_H320['W_mean'].iloc[z_index], 
    ])

    colorArray = [
        ColorList2[COLOR_H_AR1],
        ColorList2[COLOR_H_AR25],
        ColorList2[COLOR_H_AR4],

        ColorList2[COLOR_H_AR1+1],
        ColorList2[COLOR_H_AR25+1],
        ColorList2[COLOR_H_AR4+1],

        ColorList2[COLOR_H_AR1+2],
        ColorList2[COLOR_H_AR25+2],
        ColorList2[COLOR_H_AR4+2],
    ]


    _err = np.array([
        expAR1_H120['W_std'].iloc[z_index],
        expAR25_H120['W_std'].iloc[z_index],
        expAR4_H120['W_std'].iloc[z_index], 
        
        expAR1_H220['W_std'].iloc[z_index],
        expAR25_H220['W_std'].iloc[z_index],
        expAR4_H220['W_std'].iloc[z_index],
        
        expAR1_H320['W_std'].iloc[z_index],
        expAR25_H320['W_std'].iloc[z_index],
        expAR4_H320['W_std'].iloc[z_index] 
    ])
    
    # p02 = axs[0, 1].get_position()
    # p12 = [p02.x0, p02.y0, p02.width, 1]
    # axs[0, 1].set_position(p12)
    x_pos = np.flip(np.array([0,0.5,1,2,2.5,3,4,4.5,5]))
    labels = ('$AR_{1-120}$','$AR_{1-220}$','$AR_{1-320}$',
              '$AR_{2.5-120}$','$AR_{2.5-220}$','$AR_{2.5-320}$',
              '$AR_{4-120}$','$AR_{4-220}$','$AR_{4-320}$')
    rects = ax2.barh(x_pos,fullFactor,color = colorArray,xerr=_err,height=0.5,zorder=3)
    bar_add_annotation(ax2,10,[1,3],0.012651297225629864,
                       alpha=0.6,dh=0.03,barh=0.01, barl=0.03,hspace = -0.002,
                       fontfamily='Calibri', fontsize=30)
    # plt.plot(np.array([-0.4, .4]),[0,0], color=colorArray[0],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+1,[0,0], color=colorArray[1],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+2,[0,0], color=colorArray[2],linewidth=3)
    ax2.set_xlabel('Energy [J]',labelpad=0)
    ax2.set_ylabel('Depth [mm]')
    ax2.set_yticks(x_pos,['','120','','','220','','','330',''],rotation=90)
    #plt.minorticks_on()
    # ax2.bar_label(rects, labels = labels, color='black')
    ax2.grid(which='minor', axis='x', linestyle='--', color='gray', alpha=0.2, zorder=0)
    ax2.grid(axis='x',zorder=0,linestyle='--')
    ax2.text(0.01, .935, 'B', fontsize=60,transform=ax2.transAxes)
    plt.draw()


    #Plot horizontal asymetric
    fullFactor = np.array([
        expAR1_H120['W_mean'].iloc[z_index],
        expAR1_ASYM0_H120['W_mean'].iloc[z_index],
        expAR1_ASYM1_H120['W_mean'].iloc[z_index]
    ])

    colorArray = [
        ColorList2[COLOR_H_AR1],
        ColorList2[COLOR_H_AR1_ASYM0],
        ColorList2[COLOR_H_AR1_ASYM1],
    ]

    _err = np.array([
        expAR1_H120['W_std'].iloc[z_index],
        expAR1_ASYM0_H120['W_std'].iloc[z_index],
        expAR1_ASYM1_H120['W_std'].iloc[z_index]
    ])

    
    x_pos = [0,1,2]
    # labels = ('$AR_{1-120}$','$AR_{1-220}$','$AR_{1-320}$',
    #           '$AR_{2.5-120}$','$AR_{2.5-220}$','$AR_{2.5-320}$',
    #           '$AR_{4-120}$','$AR_{4-220}$','$AR_{4-320}$')
    labels = ('\n\n$AR_{1}$\t\t\t\t','\n\n$AR_{1A-UP}$\t\t\t','\n\n$AR_{1A-DOWN}$    ')
    rects = ax4.barh(x_pos,fullFactor,color = colorArray,capsize=10,xerr=_err,height=1,zorder=3)
    bar_add_annotation(ax4,5.2,[0,2],0.03237051806118191,
                       alpha=0.6,dh=0.03,barh=0.01, barl=0.03,hspace = 0.01,
                       fontfamily='Calibri', fontsize=30)

    # plt.plot(np.array([-0.4, .4]),[0,0], color=colorArray[0],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+1,[0,0], color=colorArray[1],linewidth=3)
    # plt.plot(np.array([-0.4, .4])+2,[0,0], color=colorArray[2],linewidth=3)
    ax4.set_xlabel('Energy [J]',labelpad=0)
    ax4.set_yticklabels([])
    ax4.set_ylabel('Depth 120mm')
    # ax4.set_yticks(x_pos,['','120mm',''],rotation=90)
    #plt.minorticks_on()
    ax4.bar_label(rects, labels = labels, label_type='center', color='black')
    ax4.grid(which='minor', axis='x', linestyle='--', color='gray', alpha=0.2, zorder=0)
    ax4.grid(axis='x',zorder=0,linestyle='--')
    ax4.text(0.01, .87, 'D', fontsize=60,transform=ax4.transAxes)
    plt.draw()

    plt.savefig("./results/Fig2_horizontal.png", dpi=300)
    #plt.show()


    print("RAW data power values")
    outnames = ["AR1 120","AR1 220","AR1 320",
                "AR25 120", "AR25 220", "AR25 320",
                "AR4 120", "AR4 220", "AR4 320",
                "AR1 DOWN","AR1 UP"]
    databloc = [expAR1_H120, expAR1_H220, expAR1_H320,
                expAR25_H120,expAR25_H220, expAR25_H320,
                expAR4_H120,expAR4_H220, expAR4_H320,
                expAR1_ASYM1_H120,expAR1_ASYM0_H120]

    for j,exp in enumerate(databloc):
        __arr = []
        for i in range(exp['N'][0]):
            __arr.append(exp['W_exp_'+str(i)].iloc[z_index])
            # print(exp['z_exp_'+str(i)].iloc[-1])
        print(outnames[j])
        print(__arr)



