lab1 = float(input("indique nota del primer laboratorio: "))

while lab1 < 1 or lab1 > 7:
    print("Valor invalido")
    lab1 = float(input("indique nota del primer laboratorio: "))

lab2 = float(input("indique nota del segundo laboratorio: "))

while lab2 < 1 or lab2 > 7:
    print("Valor invalido")
    lab2 = float(input("indique nota del segundo laboratorio: "))

lab3 = float(input("indique nota del tercer laboratorio: "))

while lab3 < 1 or lab3 > 7:
    print("Valor invalido")
    lab3 = float(input("indique nota del tercer laboratorio: "))

promedio_pon = round((lab1 * 0.3) + (lab2 * 0.4) + (lab3 * 0.3), 1)

print("el promedio es de ",promedio_pon)

if promedio_pon > 6.0:
    print("estudiente aprobó con distinción")
else:
    if promedio_pon > 4.0:
        print("estudiante aprobó")
    else:
        print("alumno reprobó")