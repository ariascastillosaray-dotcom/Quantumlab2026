#simulacion lanzamiento de una pelota
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v0 = 20
angulo = 45
angulo_rad = np.radians(angulo)
t = np.linspace(0, 3, 200)

x = v0 * np.cos(angulo_rad) * t
y = v0 * np.sin(angulo_rad) * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.title("Mov. parabólico")
plt.grid(True)
plt.show()
