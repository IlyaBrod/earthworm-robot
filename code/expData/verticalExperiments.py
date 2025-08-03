# Copyright (c) 2025 I. Brodoline. See LICENSE file for details.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from CONFIG import*
from .DATAFILES import*
from .processFunctions import*

expAR1 = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_AR1][SELECT_DENSITY])
expAR25 = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_AR25][SELECT_DENSITY])
expAR4 = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_AR4][SELECT_DENSITY])
expAR1_ASYM = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_ASYM][SELECT_DENSITY])

if(SELECT_DENSITY==DENSITY_1_42):
    expAIR = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_AIR][SELECT_DENSITY])
    expVACUUM_AR1 = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_VACUUM_AR1][SELECT_DENSITY])
    expVACUUM_AR1_REF = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_VACUUM_AR1_REF][SELECT_DENSITY])
    expVACUUM_AR25 = getExperimental(EXPERIMENT_FILES_fineSand_V[TIP_SELECT_VACUUM_AR25][SELECT_DENSITY])
    