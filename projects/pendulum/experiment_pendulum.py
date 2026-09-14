import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
g = 9.81
L = 1.0

# Initial conditions
theta = np.radians(30)
omega = 0

# Time
dt = 0.01
t = np.arange(0, 10, dt)

angles = []
angular_velocities = []

for time in t:
    angles.append(theta)
    angular_velocities.append(omega)

    alpha = -(g / L) * np.sin(theta)

    theta += omega * dt
    omega += alpha * dt

plt.plot(t, angles)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Simple Pendulum')
plt.grid(True)
plt.show()
