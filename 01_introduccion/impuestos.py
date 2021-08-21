edad = int(input("¿Cuál es tu edad?"))
ingresos = float(input("¿Cuales son tus ingresos mensuales?"))

if (edad > 16 and ingresos >= 1000): # && -> and, || -> or, ! -> not, != -> != 
    print("Tienes que cotizar")
    print("ADIOS")
else:
    print("No tienes que cotizar")
    print("Aun...")

print("Fin del programa")
