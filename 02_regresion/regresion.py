import math

x = []
y = []
promedio_x = 0
promedio_y = 0
sumatoria_xy = 0
sumatoria_xx = 0
sumatoria_yy = 0
b0 = 0
b1 = 0
n = 0

n = int(input("Tamaño de la lista: "))

print("Introduce los elementos de x[]")

for i in range(n):
    x.append(float(input("x[%d]: "% i)))
    promedio_x = promedio_x + x[i]

print("Introduce los elementos de y[]")

for i in range(n):
    y.append(float(input("y[%d]: "% i)))
    promedio_y = promedio_y + y[i]

promedio_x = promedio_x / n
promedio_y = promedio_y / n
print("Promedio X: %f"% promedio_x)
print("Promedio Y: %f"% promedio_y)

for i in range(n):
    sumatoria_xx = sumatoria_xx + x[i]**2
    sumatoria_xy = sumatoria_xy + x[i] * y[i]
    sumatoria_yy = sumatoria_yy + y[i]**2

b1 = (sumatoria_xy - (n * promedio_x * promedio_y)) / (sumatoria_xx - (n * promedio_x**2))
b0 = promedio_y - (b1 * promedio_x)

print(b1)
print(b0)