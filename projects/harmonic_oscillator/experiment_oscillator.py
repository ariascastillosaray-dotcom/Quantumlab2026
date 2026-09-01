import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
m = 1
k = 1

# Initial conditions
x = 1
v = 0

# Time
dt = 0.01
t = np.arange(0, 20, dt)

positions = []
velocities = []

for time in t:
    positions.append(x)
    velocities.append(v)

    # Update position and velocity using Euler's method
    a = -k/m * x  # Acceleration from Hooke's law
    x += v * dt
    v += a * dt
plt.figure(figsize=(10, 6))
plt.plot(t, positions, label='Position')
plt.plot(t, velocities, label='Velocity')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()