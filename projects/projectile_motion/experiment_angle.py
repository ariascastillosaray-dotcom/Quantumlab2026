import numpy as np
import matplotlib.pyplot as plt

g = -9.81
v0 = 20

launch_angles = []
ranges = []

for angle in np.arange(0, 91, 5):
    angle_rad = np.radians(angle)

    px = 0
    py = 0

    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)

    dt = 0.01

    while py >= 0:
        px = px + vx * dt
        py = py + vy * dt

        vy = vy + g * dt

    launch_angles.append(angle)
    ranges.append(px)

    max_index = np.argmax(ranges)
    best_angle = launch_angles[max_index]
    max_range = ranges[max_index]

print(f"Best angle: {best_angle} degrees")
print(f"Maximum range: {max_range:.3f} m")

plt.plot(launch_angles, ranges)
plt.xlabel('Launch Angle (degrees)')
plt.ylabel('Range (m)')
plt.title('Range vs Launch Angle')
plt.grid(True)
plt.show()