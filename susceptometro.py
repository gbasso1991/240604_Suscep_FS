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
def lector(file):
    with open(file, 'rb') as f:
        codificacion = chardet.detect(f.read())['encoding']
    data=pd.read_csv(os.path.join(os.getcwd(),file),skiprows=3,
                        usecols=(0,1,2,3,4),
                        decimal='.',engine='python',
                        encoding=codificacion,
                        names=('F','V','V"','X','X"'))

#                        dtype={'Tiempo_(s)':'float','Campo_(kA/m)':'float','Magnetizacion_(A/m)':'float'})  
    f= pd.Series(data['F']).to_numpy(dtype=float)
    X= pd.Series(data['X']).to_numpy(dtype=float)
    X_2= pd.Series(data['X"']).to_numpy(dtype=float)

    return f,X,X_2
#%% Perpendicular
fig, (ax,ax2,ax3) = plt.subplots(nrows=3,figsize=(7,8),sharex=True,constrained_layout=True)
for file in glob.glob('**/*P*'):
    name=file.split('/')[-1][:-4]
    F,X,X_2=lector(file)
    #phi=X_2/x
    ax.plot(F,X,'o-',label=name)
    ax2.plot(F,X_2,'o-',label=name)
    ax3.plot(F,X_2/X,'o-',label=name)
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
ax3.set_xlabel('f (Hz)') 

for i in [ax,ax2,ax3]:
    i.legend(ncol=2)
    i.set_xscale('log')
    i.grid()
plt.suptitle('Susceptibilidad vs frecuencia - Perpendicular',fontsize=15)
#%% Axial
fig, (ax,ax2,ax3) = plt.subplots(nrows=3,figsize=(7,8),sharex=True,constrained_layout=True)
for file in glob.glob('**/*A*'):
    name=file.split('/')[-1][:-4]
    F,X,X_2=lector(file)
    #phi=X_2/x
    ax.plot(F,X,'o-',label=name)
    ax2.plot(F,X_2,'o-',label=name)
    ax3.plot(F,X_2/X,'o-',label=name)
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
ax3.set_xlabel('f (Hz)') 

for i in [ax,ax2,ax3]:
    i.legend(ncol=2)
    i.set_xscale('log')
    i.grid()
plt.suptitle('Susceptibilidad vs frecuencia - Axial',fontsize=15)

#%% Random
fig, (ax,ax2,ax3) = plt.subplots(nrows=3,figsize=(7,8),sharex=True,constrained_layout=True)
for file in glob.glob('**/*R*'):
    name=file.split('/')[-1][:-4]
    F,X,X_2=lector(file)
    #phi=X_2/x
    ax.plot(F,X,'o-',label=name)
    ax2.plot(F,X_2,'o-',label=name)
    ax3.plot(F,X_2/X,'o-',label=name)
    print(file)
ax.set_ylabel(r'$\chi$')
ax2.set_ylabel(r'$\chi$"')
ax3.set_ylabel(r'$\chi$"')
ax3.set_xlabel('f (Hz)') 

for i in [ax,ax2,ax3]:
    i.legend(ncol=2)
    i.set_xscale('log')
    i.grid()
plt.suptitle('Susceptibilidad vs frecuencia - Random',fontsize=15)
# %%
