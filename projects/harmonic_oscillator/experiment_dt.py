import numpy as np
import matplotlib.pyplot as plt

# Physical parameters
m = 1
k = 1

# Initial conditions
x0 = 1
v0 = 0

# Simulation time
t_max = 20

dt_values = []
energy_errors = []

for dt in [0.1, 0.05, 0.02, 0.01, 0.005]:
    x = x0
    v = v0
    t = np.arange(0, t_max, dt)

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

    # Calculate energy error
    E_initial = 0.5 * m * v0**2 + 0.5 * k * x0**2
    energy_error = np.abs(total_energy[-1] - E_initial) / E_initial * 100  # Percentage error
    dt_values.append(dt)
    energy_errors.append(energy_error)

    print(f"dt = {dt} -> Energy error = {energy_error:.3f}%")
    
plt.plot(dt_values, energy_errors, marker='o')
plt.xlabel('Time step (dt)')
plt.ylabel('Energy error (%)')
plt.title('Energy Error vs Time Step')
plt.grid(True)
plt.show()
