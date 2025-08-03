# Copyright (c) 2025 I. Brodoline. See LICENSE file for details.

import pandas as pd
import numpy as np
from scipy.signal import medfilt,decimate
from scipy.interpolate import interp1d
def getRFactor(factor,ref):
    """Calculate relative factor, comparing energy values

    Args:
        factor (Dataframe): evaluated values
        ref (Dataframe): reference values

    Returns:
        _type_: factor in percents
    """
    return np.round((ref-factor)/ref*100,0)

def getWork(dataframe,**kwargs):
    """Rigid penetration:
     Force work [Joule] = Force[idepth] * step
    The sum of every step = distance of penetration

    Args:
        dataframe (pd.Dataframe): dataframe containing the penetration force data.
        **kwargs = ['depth' in mm]

    Returns:
        _type_: updates dataframe with 'W_med', 'W_max' and 'W_min' in [Joules]
    """
    keysList = list(dataframe.keys())

    offset = kwargs.get('offset',0)
    z_index = dataframe.index.tolist()

    if('med' in keysList):
        for z_index_i in z_index:
            dataframe.loc[z_index_i,'W_med'] = np.trapz(dataframe['med'].iloc[:z_index_i],
                                                        dataframe['z'].iloc[:z_index_i]*1e-3) + offset
    
    if('max' in keysList):
        for z_index_i in z_index:
            dataframe.loc[z_index_i,'W_max'] = np.trapz(dataframe['max'].iloc[:z_index_i],
                                                        dataframe['z'].iloc[:z_index_i]*1e-3) + offset

    if('min' in keysList):
        for z_index_i in z_index:
            dataframe.loc[z_index_i,'W_min'] = np.trapz(dataframe['min'].iloc[:z_index_i],
                                                        dataframe['z'].iloc[:z_index_i]*1e-3) + offset

    if('N' in keysList):
        for i in range(dataframe['N'][0]):
            for z_index_i in z_index:
                dataframe.loc[z_index_i,"W_exp_" + str(i)] = np.trapz(dataframe["exp_"+str(i)].iloc[:z_index_i],
                                                                dataframe['z'].iloc[:z_index_i]*1e-3) + offset
            #dataframe["W_exp_" + str(i)] = np.trapz(dataframe["exp_"+str(i)][dataframe['z']<=depth],dataframe['z'][dataframe['z']<=depth]*1e-3)
        
        dataframe['W_mean'] = np.mean([dataframe['W_exp_' + str(i)].values for i in range(dataframe['N'][0])], axis=0)
        dataframe['W_std'] = np.std([dataframe['W_exp_' + str(i)].values for i in range(dataframe['N'][0])], axis=0,ddof=1) # / dataframe['N'][0]   
        dataframe['W_p_std'] = dataframe['W_mean'] + dataframe['W_std']
        dataframe['W_m_std'] = dataframe['W_mean'] - dataframe['W_std']
    return dataframe

def getExperimental(filepathList):

    expNbr = len(filepathList)
    expData = []
    for i in range(expNbr):
        expData.append(pd.read_csv(filepathList[i]))

    expDataSize = list(len(df['force'].values) for df in expData)
    dataCrop = min(expDataSize)

    #Clean data
    return_table = dict()
    medKernel = 5
    for i,data in enumerate(expData):
        data['force'] = medfilt(data['force'], kernel_size=medKernel)  # Apply median filter
        data['force'] = data['force'][0:-medKernel]
        data.loc[data['force']<0,'force'] = 0 #cancel negative values

    dataCrop -= medKernel
    
    #Extract indicators
    exp_depth = expData[0]['steps'].values[:dataCrop]
    exp_max = np.maximum.reduce([df['force'].values[:dataCrop] for df in expData])
    exp_min = np.minimum.reduce([df['force'].values[:dataCrop] for df in expData])
    exp_med = np.median([df['force'].values[:dataCrop] for df in expData], axis=0)
    exp_mean = np.mean([df['force'].values[:dataCrop] for df in expData], axis=0)
    exp_std = np.std([df['force'].values[:dataCrop] for df in expData], axis=0,ddof=1) #/np.sqrt(expNbr)
    
    return_table = {'z': exp_depth, 
                    'med': exp_med, 
                    'max': exp_max, 
                    'min': exp_min,
                    'p_std' : exp_mean + exp_std,
                    'm_std' : exp_mean - exp_std,
                    'std' : exp_std,
                    'mean' : exp_mean,
                    'N': np.ones(np.size(exp_min))*expNbr}

    for i in range(expNbr):
        return_table["exp_" + str(i)] = expData[i]['force'].values[:dataCrop]
        return_table["z_exp_" + str(i)] = expData[i]['steps'].values[:dataCrop]

    dataframe = pd.DataFrame(return_table)
    dataframe['N'] = dataframe['N'].astype(int)

    return dataframe

def synch_rates(data, time, time_ref):
    """
    Interpolates data to the same time base as time_ref.

    Parameters:
        data (np.ndarray): array containing the data to interpolate
        time (np.ndarray): time array of the data to interpolate
        time_ref (str): target time vector

    Returns:
        data_synched_up (np.ndarray): Interpolated values of data on the time base of time_ref.

    Example:
        data1 = np.array([1,2,3,4,5])
        time1 = np.array([0,1,2,3,4])
        data2 = np.array([1,2,3,4,5,2,6,3,8,5])
        time2 = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5])
        new_time, new_data = synch_sampling_rate(data2,time2,data1,time1)
        print(new_time, new_data)
        >> [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5] [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5]
    """

    # Identify the data required to be resampled
    interpolator = interp1d(time, data, axis=0, kind='linear', fill_value='extrapolate')
    interpolated_values = interpolator(time_ref)
    return interpolated_values


def getFrictionFromSimulation(simData, expData):
    """Return the simulation data with friction scaled to the mean experiment data
    based on the ratio of skin friciton and penetraiton resistance.
    Args:
        simData (pd.Dataframe): simulation data, should contain "depth", "force_z" and "skinFriction"
        expData (pd.Dataframe): experimental data, should contain 'mean'
    """
    # print(expData['mean'].tolist())

    friction_ratio = simData['skinFriction'] / (simData['force_z'] + simData['skinFriction'])
    friction_ratio = friction_ratio.fillna(0)
    exp_force = synch_rates(expData['mean'].tolist(),expData['z'].tolist(),simData['depth'].tolist())
    exp_force[np.isnan(exp_force)] = 0

    return exp_force * friction_ratio
    
