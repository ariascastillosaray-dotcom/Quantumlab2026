import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 500) #ponemos2pi para que salga el ciclo completo
y = np.sin(x)
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("sin(x)") #si fuese seno de 2x entonces aumento la frecuencia
#si fuese 2*seno(x) entonces aumento la amplitud
plt.title("Función seno")
plt.grid(True)
plt.show()