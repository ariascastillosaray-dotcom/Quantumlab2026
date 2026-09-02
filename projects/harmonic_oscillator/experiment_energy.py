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

kinetic_energy = []
potential_energy = []
total_energy = []

for time in t:
    # Calculate energies
    ke = 0.5 * m * v**2
    pe = 0.5 * k * x**2
    te = ke + pe

    kinetic_energy.append(ke)
    potential_energy.append(pe)
    total_energy.append(te)

    # Update position and velocity using Euler's method
    a = -k/m * x  # Acceleration from Hooke's law
    x += v * dt
    v += a * dt

# Plot the energies
plt.figure(figsize=(10, 6))
plt.plot(t, kinetic_energy, label='Kinetic Energy')
plt.plot(t, potential_energy, label='Potential Energy')
plt.plot(t, total_energy, label='Total Energy')
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy of a Harmonic Oscillator')
plt.legend()
plt.grid(True)
plt.show()