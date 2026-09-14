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

angles_full = []
angles_small = []
