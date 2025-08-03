#Files definition
# Example:
# EXPERIMENT_FILES[TIP_SELECT_AR1][DENSITY_1_42]
# DENSITY_1_42 = 0
# DENSITY_1_48 = 1
# DENSITY_1_54 = 2
# DENSITY_1_60 = 3


#General
TIP_SELECT_AR1 = 0
TIP_SELECT_AR25 = 1
TIP_SELECT_AR4 = 2

#Horizontal
TIP_SELECT_ASYM_HUP = 3
TIP_SELECT_ASYM_HDOWN = 4
TIP_SELECT_ASYM_HSIDE = 5

#Vertical
TIP_SELECT_ASYM = 3
TIP_SELECT_AIR = 4
TIP_SELECT_VACUUM_AR1 = 5
TIP_SELECT_VACUUM_AR25 = 6
TIP_SELECT_VACUUM_AR1_REF = 7

#Constant density 1.57g/cm^3
DEPTH_120 = 0 #120mm
DEPTH_220 = 1 #220mm
DEPTH_320 = 2 #320mm

#,
#         #"./expData/Vertical/AR1/Density1/PR0.5/ThesisResults_AR1_D1_PR0.5_3.csv"

EXPERIMENT_FILES_fineSand_V = [ 
    [
        ["./expData/Vertical/AR1/Density1/PR0.5/ThesisResults_AR1_D1_PR0.5_1.csv",
         "./expData/Vertical/AR1/Density1/PR0.5/ThesisResults_AR1_D1_PR0.5_2.csv",
         "./expData/Vertical/AR1/Density1/PR0.5/ThesisResults_AR1_D1_PR0.5_3.csv"],
        ["./expData/Vertical/AR1/Density2/PR0.5/ThesisResults_AR1_D2_PR0.5_1.csv",
         "./expData/Vertical/AR1/Density2/PR0.5/ThesisResults_AR1_D2_PR0.5_2.csv",
         "./expData/Vertical/AR1/Density2/PR0.5/ThesisResults_AR1_D2_PR0.5_3.csv"],
        ["./expData/Vertical/AR1/Density3/PR0.5/ThesisResults_AR1_D3_PR0.5_1.csv",
         "./expData/Vertical/AR1/Density3/PR0.5/ThesisResults_AR1_D3_PR0.5_2.csv",
         "./expData/Vertical/AR1/Density3/PR0.5/ThesisResults_AR1_D3_PR0.5_3.csv"],
        ["./expData/Vertical/AR1/Density4/PR0.5/ThesisResults_AR1_D4_PR0.5_1.csv",
         "./expData/Vertical/AR1/Density4/PR0.5/ThesisResults_AR1_D4_PR0.5_2.csv",
         "./expData/Vertical/AR1/Density4/PR0.5/ThesisResults_AR1_D4_PR0.5_3.csv"]
    ],
    [
        ["./expData/Vertical/AR2.5/Density1/PR0.5/ThesisResults_AR2.5_D1_PR0.5_1.csv",
         "./expData/Vertical/AR2.5/Density1/PR0.5/ThesisResults_AR2.5_D1_PR0.5_2.csv",
         "./expData/Vertical/AR2.5/Density1/PR0.5/ThesisResults_AR2.5_D1_PR0.5_3.csv"],
        ["./expData/Vertical/AR2.5/Density2/PR0.5/ThesisResults_AR2.5_D2_PR0.5_1.csv",
         "./expData/Vertical/AR2.5/Density2/PR0.5/ThesisResults_AR2.5_D2_PR0.5_2.csv",
         "./expData/Vertical/AR2.5/Density2/PR0.5/ThesisResults_AR2.5_D2_PR0.5_3.csv"],
        ["./expData/Vertical/AR2.5/Density3/PR0.5/ThesisResults_AR2.5_D3_PR0.5_1.csv",
         "./expData/Vertical/AR2.5/Density3/PR0.5/ThesisResults_AR2.5_D3_PR0.5_2.csv",
         "./expData/Vertical/AR2.5/Density3/PR0.5/ThesisResults_AR2.5_D3_PR0.5_3.csv"],
        ["./expData/Vertical/AR2.5/Density4/PR0.5/ThesisResults_AR2.5_D4_PR0.5_1.csv",
         "./expData/Vertical/AR2.5/Density4/PR0.5/ThesisResults_AR2.5_D4_PR0.5_2.csv",
         "./expData/Vertical/AR2.5/Density4/PR0.5/ThesisResults_AR2.5_D4_PR0.5_3.csv"]
    ],
    [
        ["./expData/Vertical/AR4/Density1/PR0.5/ThesisResults_AR4_D1_PR0.5_1.csv",
         "./expData/Vertical/AR4/Density1/PR0.5/ThesisResults_AR4_D1_PR0.5_2.csv",
         "./expData/Vertical/AR4/Density1/PR0.5/ThesisResults_AR4_D1_PR0.5_3.csv"],
        ["./expData/Vertical/AR4/Density2/PR0.5/ThesisResults_AR4_D2_PR0.5_1.csv",
         "./expData/Vertical/AR4/Density2/PR0.5/ThesisResults_AR4_D2_PR0.5_2.csv",
         "./expData/Vertical/AR4/Density2/PR0.5/ThesisResults_AR4_D2_PR0.5_3.csv"],
        ["./expData/Vertical/AR4/Density3/PR0.5/ThesisResults_AR4_D3_PR0.5_1.csv",
         "./expData/Vertical/AR4/Density3/PR0.5/ThesisResults_AR4_D3_PR0.5_2.csv",
         "./expData/Vertical/AR4/Density3/PR0.5/ThesisResults_AR4_D3_PR0.5_3.csv"],
        ["./expData/Vertical/AR4/Density4/PR0.5/ThesisResults_AR4_D4_PR0.5_1.csv",
         "./expData/Vertical/AR4/Density4/PR0.5/ThesisResults_AR4_D4_PR0.5_2.csv",
         "./expData/Vertical/AR4/Density4/PR0.5/ThesisResults_AR4_D4_PR0.5_3.csv"]
    ],
    [
        ["./expData/Vertical/ASYM/Density1/ThesisResults_ASYM_D1_PR0.5_1.csv",
         "./expData/Vertical/ASYM/Density1/ThesisResults_ASYM_D1_PR0.5_2.csv",
         "./expData/Vertical/ASYM/Density1/ThesisResults_ASYM_D1_PR0.5_3.csv"],
        ["./expData/Vertical/ASYM/Density2/ThesisResults_ASYM_D2_PR0.5_1.csv",
         "./expData/Vertical/ASYM/Density2/ThesisResults_ASYM_D2_PR0.5_2.csv",
         "./expData/Vertical/ASYM/Density2/ThesisResults_ASYM_D2_PR0.5_3.csv"],
        ["./expData/Vertical/ASYM/Density3/ThesisResults_ASYM_D3_PR0.5_1.csv",
         "./expData/Vertical/ASYM/Density3/ThesisResults_ASYM_D3_PR0.5_2.csv",
         "./expData/Vertical/ASYM/Density3/ThesisResults_ASYM_D3_PR0.5_3.csv"],
        ["./expData/Vertical/ASYM/Density4/ThesisResults_ASYM_D4_PR0.5_1.csv",
         "./expData/Vertical/ASYM/Density4/ThesisResults_ASYM_D4_PR0.5_2.csv",
         "./expData/Vertical/ASYM/Density4/ThesisResults_ASYM_D4_PR0.5_3.csv"]
    ],
    [
        ["./expData/Vertical/AIR/Density1/FR2_Air2_0.csv",
         "./expData/Vertical/AIR/Density1/FR2_Air2_1.csv",
         "./expData/Vertical/AIR/Density1/FR2_Air2_2.csv",
         "./expData/Vertical/AIR/Density1/FR2_Air2_3.csv"],
    ],
    [
        ["./expData/Vertical/VACUUM/Density1/TRY2/AR1_VCC_1mms_8gps_0.csv",
         "./expData/Vertical/VACUUM/Density1/TRY2/AR1_VCC_1mms_8gps_1.csv"]
    ],
    [
        ["./expData/Vertical/VACUUM/Density1/TRY1/AR2.5_VacuumASP_0.csv",
         "./expData/Vertical/VACUUM/Density1/TRY1/AR2.5_VacuumASP_1.csv",
         "./expData/Vertical/VACUUM/Density1/TRY1/AR2.5_VacuumASP_2.csv",
         "./expData/Vertical/VACUUM/Density1/TRY1/AR2.5_VacuumASP_3.csv",
         "./expData/Vertical/VACUUM/Density1/TRY1/AR2.5_VacuumASP_4.csv"]
    ],
    [
        ["./expData/Vertical/VACUUM/Density1/TRY2/AR1_5mms_3.csv",
         "./expData/Vertical/VACUUM/Density1/TRY2/AR1_5mms_4.csv",
         "./expData/Vertical/VACUUM/Density1/TRY2/AR1_5mms_5.csv",
         "./expData/Vertical/VACUUM/Density1/TRY2/AR1_5mms_6.csv"]
    ]

]

EXPERIMENT_FILES_fineSand_H = [
    [
        ["./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_5.csv",
         "./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_6.csv",
         "./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_7.csv",
         "./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_8.csv",
         "./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_9.csv",
         "./expData/Horizontal/AR1/Density1/Depth1/ThesisResults_AR1_D1_Depth1_10.csv"],
        ["./expData/Horizontal/AR1/Density1/Depth2/ThesisResults_AR1_D1_Depth2_2.csv",
         "./expData/Horizontal/AR1/Density1/Depth2/ThesisResults_AR1_D1_Depth2_3.csv",
         "./expData/Horizontal/AR1/Density1/Depth2/ThesisResults_AR1_D1_Depth2_4.csv",
         "./expData/Horizontal/AR1/Density1/Depth2/ThesisResults_AR1_D1_Depth2_5.csv"],
        ["./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_5.csv",
         "./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_6.csv",
         "./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_7.csv",
         "./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_9.csv",
         "./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_10.csv",
         "./expData/Horizontal/AR1/Density1/Depth3/ThesisResults_AR1_D1_Depth3_11.csv"]
    ],
    [
        ["./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_1.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_2.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_3.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_4.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_5.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_6.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth1/ThesisResults_AR2.5_D1_Depth1_7.csv"],
        ["./expData/Horizontal/AR2.5/Density1/Depth2/ThesisResults_AR2.5_D1_Depth2_1.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth2/ThesisResults_AR2.5_D1_Depth2_2.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth2/ThesisResults_AR2.5_D1_Depth2_3.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth2/ThesisResults_AR2.5_D1_Depth2_4.csv"],
        ["./expData/Horizontal/AR2.5/Density1/Depth3/ThesisResults_AR2.5_D1_Depth3_1.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth3/ThesisResults_AR2.5_D1_Depth3_2.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth3/ThesisResults_AR2.5_D1_Depth3_3.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth3/ThesisResults_AR2.5_D1_Depth3_4.csv",
         "./expData/Horizontal/AR2.5/Density1/Depth3/ThesisResults_AR2.5_D1_Depth3_5.csv"]
    ],
    [
        ["./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_17.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_18.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_19.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_20.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_21.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_22.csv",
         "./expData/Horizontal/AR4/Density1/Depth1/ThesisResults_AR4_D1_Depth1_23.csv"],
        ["./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_2.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_3.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_4.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_5.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_6.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_7.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_8.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_9.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_10.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_11.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_12.csv",
         "./expData/Horizontal/AR4/Density1/Depth2/ThesisResults_AR4_D1_Depth2_13.csv"],
        ["./expData/Horizontal/AR4/Density1/Depth3/ThesisResults_AR4_D1_Depth3_4.csv",
         "./expData/Horizontal/AR4/Density1/Depth3/ThesisResults_AR4_D1_Depth3_5.csv",
         "./expData/Horizontal/AR4/Density1/Depth3/ThesisResults_AR4_D1_Depth3_7.csv",
         "./expData/Horizontal/AR4/Density1/Depth3/ThesisResults_AR4_D1_Depth3_8.csv"]
    ],
    [
        ["./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_1.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_2.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_3.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_4.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_5.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_6.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_7.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_8.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_9.csv",
         "./expData/Horizontal/ASYM/Density1/Depth1/ThesisResults_ASYM_D1_Depth1_10.csv"],
        ["./expData/Horizontal/ASYM/Density1/Depth2/ThesisResults_ASYM_D1_Depth2_5.csv",
         "./expData/Horizontal/ASYM/Density1/Depth2/ThesisResults_ASYM_D1_Depth2_6.csv",
         "./expData/Horizontal/ASYM/Density1/Depth2/ThesisResults_ASYM_D1_Depth2_7.csv",
         "./expData/Horizontal/ASYM/Density1/Depth2/ThesisResults_ASYM_D1_Depth2_8.csv"],
        ["./expData/Horizontal/ASYM/Density1/Depth3/ThesisResults_ASYM_D1_Depth3_1.csv",
         "./expData/Horizontal/ASYM/Density1/Depth3/ThesisResults_ASYM_D1_Depth3_2.csv",
         "./expData/Horizontal/ASYM/Density1/Depth3/ThesisResults_ASYM_D1_Depth3_3.csv",
         "./expData/Horizontal/ASYM/Density1/Depth3/ThesisResults_ASYM_D1_Depth3_4.csv",
         "./expData/Horizontal/ASYM/Density1/Depth3/ThesisResults_ASYM_D1_Depth3_5.csv"]
    ],
    [
        ["./expData/Horizontal/ASYMDown/ThesisResults_ASYMDown_D1_Depth1_1.csv",
         "./expData/Horizontal/ASYMDown/ThesisResults_ASYMDown_D1_Depth1_2.csv",
         "./expData/Horizontal/ASYMDown/ThesisResults_ASYMDown_D1_Depth1_3.csv"]
    ],
    [
        ["./expData/Horizontal/ASYMSide/Depth1/ThesisResults_ASYMOLd_D1_Depth1_1.csv",
         "./expData/Horizontal/ASYMSide/Depth1/ThesisResults_ASYMOLd_D1_Depth1_3.csv",
         "./expData/Horizontal/ASYMSide/Depth1/ThesisResults_ASYMOLd_D1_Depth1_4.csv"]
    ],


]