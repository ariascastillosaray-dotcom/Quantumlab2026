import numpy as np
import matplotlib.pyplot as plt
masas = np.array([63, 70, 55, 81, 92])
gravedad = 9.81
pesos = masas * gravedad
plt.plot(masas, pesos, marker="o") #plt.scatter representa sin unir los puntos
#lo de marker hace que se vea el puntito en la linea, sino lo pongo solo se ve la linea
plt.title("Pesos de acuerdo a distintas masas")
plt.xlabel("Masa (kg)")
plt.ylabel("Peso (N)")
plt.grid(True)#esto es la cuadricula de fondo
plt.show()
