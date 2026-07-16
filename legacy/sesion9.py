
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 500)
y = np.sin(x)
dy = np.gradient(y, x) #le das valores y e x y te devuelve la derivada de y con respecto a x
plt.plot(x, y, label="sin(x)")
plt.plot(x, dy, label="Derivada")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Seno y su derivada")
plt.grid(True)
plt.legend()
plt.show()