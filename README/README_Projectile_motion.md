# Quantumlab2026
Learning computational physics through quantum mechanics


## Projectile_motion/EXPERIMENT_DT
We wanted to see how the size of the temporal step can affect to the precission in a simulated parabolic movement

Hipothesis:
    If we reduce the size of the temporal step (dt), it should let us be closer to the exact solution
Method:
    Simulation through Euler method
    Without friction
    Initial velocity = 20 m/s
    Angle = 45 degrees
    Comparison with the exact solution
Results:
    The trajectories converge
    The range is getting closer to the exact value
    The relative error decreases when we reduce dt
Conclusion:
    The Euler method converges when we reduce dt at the cost of increased computation time


### Projectile_motion/EXPERIMENT_ANGLE
The objective is to study how the lunch angle affects the horizontal range of the projectile. The projectile is launched with a fixed initial velocity, while the launch angle can vary between 0º and 90º. For each angle we use the Euler method in order to simulate the trajectories.

Method:
    We descomposed the initial velocity in vertical and horizontal components. For each launch angle, the simulation continues until the projectile reaches the ground. The final horizontal position it's the simulated range. 
    The time step taken is: dt=0.01s
Results:
    The results show that the range increases as the launch angle approaches 45º and decreases afterwards.
    -Optimal launch angle: 45º
    -Maximum simulated range: 41.012m
    This are the results we waited, thanks to the theorical prediction that the maximum range, for a projectile launched and landing at the same height occurs at an angle of 45º
    The theorical range is given by:
    R= v0^2 sin(2θ)/|g|
        For: θ=45º
        g=9.81 m/s^2
        v0=20 m/s
    The theorical range is approximately: 40.77 m

Conclusion:
    We have demonstrate numerically how the launch angle affects the range of a projectile. And the experiment successfully reproduces the expected physical behavior, with the maximum range occuring at 45º


#### Projectile_motion/EXPERIMENT_ERROR
The goal of the experiment is to study how can affect dt to the numerical error of the Euler method

Method:
    Simulate projectile motion with different dt values and compare de analytical solution with the numerical range.

Results:
    Decreasing dt decreases numerical error.
    dt = 0.5s -> Error = 8.723m
    dt = 0.01s -> Error = 0.273

Conclusion:
    Smaller time steps gives us a more accurate solution, but we are using more computational steps
