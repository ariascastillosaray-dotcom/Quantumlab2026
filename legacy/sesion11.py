import numpy as np
import matplotlib.pyplot as plt

dt = 0.01

g = -9.81

t = np.arange(0,4,dt)#sirve para crear un vector de tiempo desde 0 hasta 4 con pasos de dt

x = [] #sirve para almacenar las posiciones en x
y = []

vx = 10
vy = 20

px = 0 #es la posicion inicial en x
py = 0 #es la posicion inicial en y

for tiempo in t:

    x.append(px) #el append sirve para ir agregando los valores de px a la lista x 
    y.append(py)

    px = px + vx*dt
    py = py + vy*dt

    vy = vy + g*dt

plt.plot(x,y)

plt.grid()

plt.xlabel("x (m)")
plt.ylabel("y (m)")

plt.show()
