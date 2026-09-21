import numpy as np
import matplotlib.pyplot as plt

g = 9.81
L = 1.0

theta = np.radians(30)
omega = 0

dt = 0.01
t = np.arange(0, 10, dt)

kinetic_energy = []
potential_energy = []
total_energy = []

for time in t:
    kinetic_energy.append(0.5 * (L * omega) ** 2)
    potential_energy.append(g * L * (1 - np.cos(theta)))
    total_energy.append(kinetic_energy[-1] + potential_energy[-1])

    alpha = -(g / L) * np.sin(theta)

    theta += omega * dt
    omega += alpha * dt

plt.plot(t, kinetic_energy, label='Kinetic Energy')
plt.plot(t, potential_energy, label='Potential Energy')
plt.plot(t, total_energy, label='Total Energy')

plt.xlabel('Time (s)')
plt.ylabel('Energy (J)')
plt.title('Energy of a Simple Pendulum')
plt.legend()
plt.grid(True)
plt.show()