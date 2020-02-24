# Code source: Jaques Grobler
# License: BSD 3 clause

#Se cargan los modulos

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Se cargan los datos
diabetes = datasets.load_diabetes()


# Se usa cierta muestra de los datos
diabetes_X = diabetes.data[:, np.newaxis]
diabetes_X_temp = diabetes_X[:, :, 2]

# Se separa la muestra de datos
diabetes_X_train = diabetes_X_temp[:-30]
diabetes_X_test = diabetes_X_temp[-30:]

# Se separa las variables explicadas
diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

# Se crean los modelos lineales
regr = linear_model.LinearRegression()
regr2=linear_model.Lasso(alpha=.5)
regr3=linear_model.Ridge(alpha=.5)

#Se entrenan los modelos
regr.fit(diabetes_X_train, diabetes_y_train)
regr2.fit(diabetes_X_train, diabetes_y_train)
regr3.fit(diabetes_X_train, diabetes_y_train)


print (u'Regresión Mínimos Cuadrados Ordinarios')
# Coeficiente
print('Coeficientes:',regr.coef_)
# MSE
print("Residual sum of squares: %.2f"
 % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Varianza explicada
print('Varianza explicada: %.2f\n' % regr.score(diabetes_X_test, diabetes_y_test))

print (u'Regresión Lasso' )
# Coeficiente
print('Coeficientes:', regr2.coef_)
# MSE
print("Residual sum of squares: %.2f"
 % np.mean((regr2.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Varianza explicada
print('Varianza explicada: %.2f\n' % regr2.score(diabetes_X_test, diabetes_y_test))

print (u'Regresión Ridge')
#Coeficiente
print('Coeficientes:', regr3.coef_)
# MSE
print("Residual sum of squares: %.2f"
 % np.mean((regr3.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Varianza explicada
print('Varianza explicada: %.2f\n' % regr3.score(diabetes_X_test, diabetes_y_test))


# Plot 
plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
 linewidth=3, label=u'Regresión MCO')
plt.plot(diabetes_X_test, regr2.predict(diabetes_X_test), color='yellow',
 linewidth=3, label=u'Regresión Lasso')
plt.plot(diabetes_X_test, regr3.predict(diabetes_X_test), color='green',
 linewidth=3, label=u'Regresión Ridge')
plt.title(u'Regresióneal por 3 metodos diferentes')
plt.legend()
plt.xticks(())
plt.yticks(())

plt.show()
