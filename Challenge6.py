#Utilizando documentación de pandas:

#Handle data
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

#Graphs
#https://matplotlib.org/stable/tutorials/introductory/pyplot.html

#1) Realizar la regresión lineal de los tests (datasets) del archivo file-load.csv (por separado). *Regresión lineal del script
#2) Generar las respectivas graficas una por una.
#3) Generar la regresión multiple para que puedan verse los historicos de examenes y la calif final.*Regresión multiple

import numpy as np
import pandas as pd
import scipy as stats
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from sklearn import linear_model

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

file = pd.read_csv('file-load-V2.csv')

datasetTest1 = file['Test1']
datasetTest2 = file['Test2']
datasetTest3 = file['Test3']
datasetTest4 = file['Test4']
datasetFinal = file['Final']
datasetLast_name=file['Last_name']

x = datasetTest4
y = datasetFinal


#REGRESION LINEAL
slope, intercept, r, p , std_err = scipy.stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc,x))

print('----------------es R-----------------------------')
print(r)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

#REGRESION MULTIPLE
""" 
v = datasetFinal
z = [[datasetTest1,datasetTest2,datasetTest3,datasetTest4]]

regr = linear_model.LinearRegression()
regr.fit(v, z)
print('--------------------REG MULTIPLE------------------------')
print(regr.coef_)
"""
#sns.set_style('darkgrid')
#nuevo datframe con njmbre nuevo
#nuevo=file[[datasetTest1,datasetTest2,datasetTest3,datasetTest4,datasetFinal,datasetLast_name]]


