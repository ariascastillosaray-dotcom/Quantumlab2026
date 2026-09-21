import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
g = 9.81
L = 1.0

# Initial conditions
theta_full = np.radians(30)
omega_full = 0

theta_small = np.radians(30)
omega_small = 0

# Time
dt = 0.01
t = np.arange(0, 10, dt)


angles_full = []
angles_small = []

for time in t:

    angles_full.append(theta_full)
    angles_small.append(theta_small)

    # Full pendulum
    alpha_full = -(g / L) * np.sin(theta_full)
    theta_full += omega_full * dt
    omega_full += alpha_full * dt

    # Small angle approximation
    alpha_small = -(g / L) * theta_small
    theta_small += omega_small * dt
    omega_small += alpha_small * dt


plt.plot(t, angles_full, label='Full pendulum')
plt.plot(t, angles_small, label='Small angle approximation')

plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Pendulum: Full vs Small Angle Approximation')
plt.legend()
plt.grid(True)
plt.show()

