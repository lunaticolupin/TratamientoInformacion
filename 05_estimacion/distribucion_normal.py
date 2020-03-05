import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt

X = ss.norm(2000,40)
x = np.arange(X.ppf(0.01),X.ppf(0.99))

plt.plot(x,X.pdf(x),"r")
plt.show()
