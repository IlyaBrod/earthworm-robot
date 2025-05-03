# Copyright (c) 2025 I. Brodoline, University of Twente. See LICENSE file for details.
from expData.DATAFILES import *

WATER_UNIT_WEIGHT = 9.81 #[kN/m^3]
G_CONSTANT = 9.80665 # m/s^2

TANK_HEIGHT = 750 #[mm]
TANK_DIAMETER = 240 #[mm]

SAND_FINE_GRAIN_DENSITY = 2.54e3 # [kg/m^3] #2.54
SAND_FINE_BULK_DENSITY = [1.42e3, 1.48e3, 1.54e3, 1.6e3] # [kg/m^3]
SAND_FINE_FRICTION = 34.2 # [deg]
SAND_FINE_INTERFACE_FRICTION = 22.6 # [deg]
SAND_FINE_VOIDRATIO_MIN = 0.6 #.45
SAND_FINE_VOIDRATIO_MAX = 0.98 #.8

SAND_COARSE_GRAIN_DENSITY = 2.54e3 # [kg/m^3] #2.54
SAND_COARSE_BULK_DENSITY = [1.42e3, 1.48e3, 1.54e3, 1.6e3] # [kg/m^3]
SAND_COARSE_FRICTION = 35.5 # [deg]
SAND_COARSE_INTERFACE_FRICTION = 28.1 # [deg]
SAND_COARSE_VOIDRATIO_MIN = 0.45 #.45
SAND_COARSE_VOIDRATIO_MAX = 0.8 #.8

#Plot colors

font = {'family' : 'Calibri',
        'weight' : 'normal',
        'size'   : 20}

COLOR_AIR = 1
COLOR_AR1 = 1
COLOR_VAC = 2
COLOR_AR25 = 3
COLOR_AR4 = 4
COLOR_AR1_ASYM = 7

ColorList = [
    "#EBB528",
    "#02B7EB",
    "#52618F",
    "#EBDB1E",
    "#2757E6",
    "#CC99FF",
    "#3A5C66",
    "#F9A825"
]

COLOR_H_AR1 = 0
COLOR_H_AR25 = 3
COLOR_H_AR4 = 6
COLOR_H_AR1_ASYM0 = 9
COLOR_H_AR1_ASYM1 = 12
ColorList2 = [
    "#FFF176",
    "#FDD835",
    "#F9A825",
    "#A5D6A7",
    "#4CAF50",
    "#2E7D32",
    "#90CAF9",
    "#2196F3",
    "#1565C0",
    "#EF9A9A",
    "#F44336",
    "#C62828",
    "#CE93D8",
    "#9C27B0",
    "#6A1B9A",
    "#B0BEC5",
    "#607D8B",
    "#37474F"
]

#Horizontal penetration density
H_DENSITY = 1.57 

#Vertical penetration density
DENSITY_1_42 = 0
DENSITY_1_48 = 1
DENSITY_1_54 = 2
DENSITY_1_60 = 3

#Select the desired density VACUUM and AIR are available only for 1_42
SELECT_DENSITY = DENSITY_1_42