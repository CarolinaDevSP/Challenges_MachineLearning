import numpy as np
import pandas as pd
import scipy as stats
import matplotlib.pyplot as plt
import scipy
file = pd.read_csv('file-load-V2.csv')

datasetFinal = file['Final']
""" 
print("--------------------------MEDIA---------------------------------")
mean = np.mean(datasetFinal)
print(mean)
print(datasetFinal.mean())

#mode=stats.mode(datasetFinal, keepdims=True)

print("--------------------------MEDIANA---------------------------------")
median = np.median(datasetFinal)
print(median)
print(datasetFinal.median())

#print(mode)
#print(datasetFinal.mode())

print("-----------------------DESVIACION STANDAR---------------------------------")
print(np.std(datasetFinal)) #desviacion standar
print(datasetFinal.std()) #con panda

print("--------------------------VARIANZA---------------------------------")
print(np.var(datasetFinal)) #varianza
print(datasetFinal.var()) #con panda

print("--------------------------PERCENTIL---------------------------------")
print(np.percentile(datasetFinal, 45)) #percentil
print(datasetFinal) #no tiene panda


x= np.random.normal(5.0,1.0,100000)
plt.hist(x,100)
plt.show()
"""
#regresion lineal-- para encontrar la relacion entre las variables
"""
x = [1,2,4,5,6,7,6,3,5,6,7,7]
y = [33,56,2,255,75,332,55,22,3,5,88,6]
"""
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

##
#*mientrars mas cerca este a la linea hay mayor probabilidad que vuelva a suceder
slope, intercept, r, p , std_err = scipy.stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc,x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

##
#challenge 6 predecir calidficacion final que es mas probabakle que se repita en el futuro
 # historico de los test
 #data set 1, datase2 , datse2 , puede ser reg lineal multiple con el recurso del profe

 


