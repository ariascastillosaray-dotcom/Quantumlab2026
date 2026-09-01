import numpy as np
import matplotlib.pyplot as plt

g = -9.81
v0 = 20
angle = 45
angle_rad = np.radians(angle)
dt_values = []
error_values = []

for dt in [0.5, 0.2, 0.1, 0.05, 0.02, 0.01]:
    x=[]
    y=[]

    px=0
    py=0

    vx = v0*np.cos(angle_rad)
    vy = v0*np.sin(angle_rad)

    while py >= 0:
        x.append(px)
        y.append(py)

        px = px + vx*dt
        py = py + vy*dt

        vy = vy + g*dt

    # analytical range for projectile on level ground: (v0^2 * sin(2*theta)) / |g|
    exact_range = (v0**2 * np.sin(2*angle_rad)) / abs(g)
    error = abs(px - exact_range)

    print(f"dt = {dt} -> Range = {px: .3f} m -> Error = {error: .3f} m")

    dt_values.append(dt)
    error_values.append(error)

plt.plot(dt_values, error_values, marker='o')
plt.xlabel("dt (s)")
plt.ylabel("Error (m)")
plt.title("Numerical Error vs Time Step")
plt.grid(True)
plt.show()
