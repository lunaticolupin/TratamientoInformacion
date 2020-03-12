import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

promedio, desviacion = 0, 0.2
normal = ss.norm(promedio, desviacion)

# ppf percent point function
x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)

# Función de Densidad de Probibilidad con Python
fp = normal.pdf(x)

plt.plot(x, fp)

plt.title("Distribución Normal")
plt.ylabel("probabilidad")
plt.xlabel("valores")
plt.show()
