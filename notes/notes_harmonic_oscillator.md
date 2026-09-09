# Quantumlab2026
Learning computational physics through quantum mechanics


## harmonic_oscillator/EXPERIMENT_OSCILLATOR
We want to simulate the motion of a harmonic oscillator using Euler's numerical method

Method:
    With the initial conditions (x=1), (v=0), (m=1) and (k=1) position and velocity were calculated over time using the equation of motion

Results:
    The simulation reproduces periodic oscillations in both (position and velocity) but we can see how the amplitude increases slightly due to numerical error

Conclusion:
    The Euler method reproduces the expected behavior, but it also includes an error that accumulate over time


### harmonic_oscillator/EXPERIMENT_ENERGY
In this expeiment we analyze the potential, kinetic, and total energy of a harmonic oscillator simulated with Euler's method

Method:
    The three energies were calculated at each time step using the numerical position and velocity

Results:
    The kinetic and potential energy oscillate continuously, while the total energy increses from 0.5 to 0.61

Conclusion:
    The total energy is not conserved due to the numerical error introduced by the Euler method. This show that the method is less accurate when we are simulating oscillatory systems over long periods