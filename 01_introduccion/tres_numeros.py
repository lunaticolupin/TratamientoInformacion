numeros = []

contador = 1

while contador <= 3:
    temp = int(input("Numero %s: " % contador))

    #if temp >= -1000 and temp <= 1000:
    if temp >= -1000:
        if temp <= 1000:
            # numeros[0] = temp
            numeros.append(temp) # agrega un elemento a la lista
            contador = contador + 1

print(numeros)
numeros.sort()
print(numeros)
