# Copyright (c) 2025 I. Brodoline. See LICENSE file for details.

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from CONFIG import*
from .DATAFILES import*
from .processFunctions import*

expAR1_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR1][DEPTH_120])
expAR1_H220 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR1][DEPTH_220])
expAR1_H320 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR1][DEPTH_320])

expAR25_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR25][DEPTH_120])
expAR25_H220 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR25][DEPTH_220])
expAR25_H320 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR25][DEPTH_320])

expAR4_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR4][DEPTH_120])
expAR4_H220 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR4][DEPTH_220])
expAR4_H320 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_AR4][DEPTH_320])

expAR1_ASYM0_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_ASYM_HUP][DEPTH_120])
expAR1_ASYM0_H220 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_ASYM_HUP][DEPTH_220])
expAR1_ASYM0_H320 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_ASYM_HUP][DEPTH_320])

expAR1_ASYM1_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_ASYM_HDOWN][DEPTH_120])
expAR1_ASYM2_H120 = getExperimental(EXPERIMENT_FILES_fineSand_H[TIP_SELECT_ASYM_HSIDE][DEPTH_120])
