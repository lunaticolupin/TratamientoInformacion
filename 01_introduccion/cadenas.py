cadena = "ejemplo de 'cadena'"
cadena1 = 'otra "cadena"'
cadena2 = "\tuna\n \"cadena\" "
acentos = "????Ñ ñ ¡¡¡ ¿¿¿ó + Ö"
curp = "XXXX210825XXXX000XXX000"

print(cadena)
print(cadena1)
print(cadena2)
print(acentos)
# print(acentos.encode('ascii'))

print(cadena1+cadena2)
print(cadena2.lower())
print(cadena2.upper())
print(cadena2.capitalize())
print(cadena2[2])
print(cadena2[2:6])
print(cadena1.replace("cadena","-"))
print("CURP: %s" % curp)
print("RFC: %s" % curp[0:10]) 
print("Fecha nacimiento: %s/%s/%s" % (curp[8:10], curp[6:8], curp[4:6]))

fecha_nacimiento = "{}-{}-{}".format(curp[8:10], curp[6:8], curp[4:6]) # Cadena con formato

print(fecha_nacimiento)
print("Fecha nacimiento: "+curp[8:10]+"/"+curp[6:8]+"/"+curp[4:6])
