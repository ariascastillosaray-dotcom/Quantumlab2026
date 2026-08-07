# Quantumlab2026
Learning computational physics through quantum mechanics


Projectile_motion/EXPERIMENT_DT
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

