materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
calificaciones = []
for subject in materias:
    score = input("¿Qué nota has sacado en " + subject + "?")
    calificaciones.append(score)
for i in range(len(materias)):
    print("En " + materias[i] + " has sacado " + calificaciones[i])
