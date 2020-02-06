edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuales son tus ingresos mensuales? "))
if edad > 16 and ingresos >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
