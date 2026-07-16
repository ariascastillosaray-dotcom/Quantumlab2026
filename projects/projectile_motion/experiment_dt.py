import numpy as np
import matplotlib.pyplot as plt

g = -9.81
v0 = 20
angle = 45
angle_rad = np.radians(angle)

dt_values = []
relative_errors = []

for dt in [0.01, 0.05, 0.1]:
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
    plt.plot(x, y, label=f"dt={dt}")
    print(f"dt = {dt} -> Range = {px: .3f} m")

    error = abs(px - exact_range)
    relative_error = error / exact_range * 100
    dt_values.append(dt)
    relative_errors.append(relative_error)

    print(f"dt = {dt}")
    print(f"  Simulated Range: {px:.3f} m")
    print(f"  Absolute Error: {error:.3f} m")
    print(f"  Relative Error: {relative_error:.2f} %")
    print()

plt.legend()
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.title("Parabolic Motion with Different dt Values")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(dt_values, relative_errors, marker='o')
plt.xlabel("dt (s)")
plt.ylabel("Relative Error (%)")
plt.title("Convergence of Euler Method")
plt.grid(True)
plt.show()