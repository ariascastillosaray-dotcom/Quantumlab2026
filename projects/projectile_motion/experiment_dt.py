import numpy as np
import matplotlib.pyplot as plt

g = -9.81
v0 = 20
angulo = 45
angulo_rad = np.radians(angulo)

for dt in [0.01, 0.05, 0.1]:
    x=[]
    y=[]

    px=0
    py=0

    vx = v0*np.cos(angulo_rad)
    vy = v0*np.sin(angulo_rad)

    while py >= 0:

        x.append(px)
        y.append(py)

        px = px + vx*dt
        py = py + vy*dt

        vy = vy + g*dt

    plt.plot(x,y,label=f"dt={dt}")
    print(f"dt = {dt} -> alcance = {px: .3f} m")

plt.legend()
plt.xlabel("Distancia (m)")
plt.ylabel("Altura (m)")
plt.title("Mov. parabólico con distintos dt")
plt.grid(True)
plt.show()
