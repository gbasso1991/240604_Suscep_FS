#%%
import numpy as np
import matplotlib.pyplot as plt
import fnmatch
import os
import pandas as pd
import chardet 
import re
from scipy.interpolate import interp1d
from uncertainties import ufloat, unumpy 
import glob
#%%
def lector_ciclos(file):
    
    data=pd.read_csv(os.path.join(os.getcwd(),file),skiprows=3,
                        usecols=(0,1,2,3,4),
                        decimal='.',engine='python',
                        names=('F','V','V"','X','X"'))

#                        dtype={'Tiempo_(s)':'float','Campo_(kA/m)':'float','Magnetizacion_(A/m)':'float'})  
    f= pd.Series(data['F']).to_numpy(dtype=float)
    X= pd.Series(data['X']).to_numpy(dtype=float)
    X_2= pd.Series(data['X"']).to_numpy(dtype=float)
    
    return f,X,X_2

# %%
A,B,C=lector_ciclos('AVSF.csv')

#%% Perpendicular
fig, (ax,ax2) = plt.subplots(nrows=2,figsize=(8,5),constrained_layout=True)
for file in glob.glob('*P*'):
    F,X,X_2=lector_ciclos(file)
    ax.plot(F,X,'.-',label=file.split('.')[0][:])
    ax2.plot(F,X_2,'.-',label=file.split('.')[0][:])
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
for i in [ax,ax2]:
    i.legend(ncol=2)
    i.grid()
    i.set_xlabel('f (Hz)')
plt.suptitle('Susceptibilidad vs frecuencia - Perpendicular')
# %%
#%% Axial
fig, (ax,ax2) = plt.subplots(nrows=2,figsize=(8,5),constrained_layout=True)
for file in glob.glob('*A*'):
    F,X,X_2=lector_ciclos(file)
    ax.plot(F,X,'.-',label=file.split('.')[0][:])
    ax2.plot(F,X_2,'.-',label=file.split('.')[0][:])
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
for i in [ax,ax2]:
    i.legend(ncol=2)
    i.grid()
    i.set_xlabel('f (Hz)')
plt.suptitle('Susceptibilidad vs frecuencia - Axial')

#%% Random
fig, (ax,ax2) = plt.subplots(nrows=2,figsize=(8,5),constrained_layout=True)
for file in glob.glob('*R*'):
    F,X,X_2=lector_ciclos(file)
    ax.plot(F,X,'.-',label=file.split('.')[0][:])
    ax2.plot(F,X_2,'.-',label=file.split('.')[0][:])
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
for i in [ax,ax2]:
    i.legend(ncol=2)
    i.grid()
    i.set_xlabel('f (Hz)')
plt.suptitle('Susceptibilidad vs frecuencia - Random')
# %%
