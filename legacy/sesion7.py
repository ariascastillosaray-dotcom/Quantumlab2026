import numpy as np
import matplotlib.pyplot as plt

masas = np.linspace(40, 100, 50)  # me da 50 valores entre 40 y 100
gravedad = 9.81
error = np.random.normal(0, 15, len(masas))  # genera error aleatorio con distribucion normal
# media=0 y desviacion tipica=15, y el len(masas) es para que de un error a cada masa
pesos = masas * gravedad + error
coeficientes = np.polyfit(masas, pesos, 1) #Ajuste lineal de grado 1
print(coeficientes)

pendiente = coeficientes[0]
ordenada = coeficientes[1]
recta = pendiente * masas + ordenada

plt.scatter(masas, pesos)
plt.plot(masas, recta)
plt.show()

