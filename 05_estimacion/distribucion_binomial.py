''' Ejemplo: Un proveedor de DVDs regrabables afirma que solamente el 4 % de los

artículos suministrados son defectuosos. Si un cliente compra un lote de 25

DVDs, ¿cuál es el número esperado de DVDs defectuosos en el lote? Si el cliente

encuentra que 4 de los DVDs comprados son defectuosos, ¿debe dudar de la

afirmación del vendedor?
'''

import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

X = ss.binom(25,0.04)
x = np.arange(10)

plt.plot(x,X.pmf(x),"bo")
plt.vlines(x,0,X.pmf(x),"b")
plt.show()

print(X.mean()) # 1.0


pr = X.sf(3)
print(pr)
