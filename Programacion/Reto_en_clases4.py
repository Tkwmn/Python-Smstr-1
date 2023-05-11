print("Ingrese datos de 3 pacientes","\n")

#----------------Paciente 1---------------#

print("PACIETE 1°","\n")
p1 = input("Ingrese el nombre: ")
peso_p1 = float(input("Indique el peso (Kg): "))

while peso_p1 < 1:
    print("Valor invalido")
    peso_p1 = float(input("Indique el peso (Kg): "))


est_p1 = float(input("Especifique estatura: "))

while est_p1 < 1:
    print("Valor invalido")
    est_p1 = float(input("Indique la estatura: "))
else:
    print("Valor Valido")

ed_p1 = int(input("¿Cuál es la edad+?: "))

while ed_p1 < 1 :
    print("Valor invalido")
    ed_p1 = int(input("¿Cuál es la edad?: "))
else:
    print("Valor valido","\n")

#-----------------Paciente 2----------------#

print("PACIETE 2°","\n")
p2 = input("Ingrese el nombre: ")

peso_p2 = float(input("Indique el peso (Kg): "))

while peso_p2 < 1:
    print("Valor invalido")
    peso_p2 = float(input("Indique el peso (Kg): "))
else:
    print("Valor Valido")

est_p2 = float(input("Especifique estatura: "))

while est_p2 < 1:
    print("Valor invalido")
    est_p2 = float(input("Indique estatura: "))
else:
    print("Valor Valido")

ed_p2 = int(input("¿Cuál es la edad?: "))

while ed_p2 < 1 :
   ed_p1 = int(input("¿Cuál es la edad: "))
else:
    print("Valor valido","\n")

#-----------------Paciente 3----------------#

print("PACIETE 3°","\n")
p3 = input("Ingrese el nombre: ")
peso_p3 = float(input("Indique el peso (Kg): "))

while peso_p3 < 1:
    print("Valor invalido")
    peso_p3 = float(input("Indique el peso (Kg): "))
else:
    print("Valor Valido")

est_p3 = float(input("Especifique estatura: "))

while est_p3 < 1:
    print("Valor invalido")
    est_p3 = float(input("Indique estatura: "))
else:
    print("Valor Valido")

ed_p3 = int(input("¿Cuál es la edad?: "))

while ed_p3 < 1 :
    ed_p1 = int(input("¿Cuál es la edad?: "))
else:
    print("Valor valido","\n")

#----------------TUPLAS---------------#

paciente1 = (p1, peso_p1, est_p1, ed_p1)
paciente2 = (p2, peso_p2, est_p2, ed_p2)
paciente3 = (p3, peso_p3, est_p3, ed_p3)

#----------------IMPRESIÓN DE TUPLAS---------#

print("             TUPLAS           ","\n")

print(paciente1,"\n")

print(paciente2,"\n")

print(paciente3,"\n")