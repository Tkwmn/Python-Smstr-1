nombre = input("Ingrese su nombre:")
asig = input("Ingrese la asignatura:")
nota1 = float(input("Ingrese primera nota de laboratorio:"))
nota2 = float(input("Ingrese segunda nota de laboratorio:"))

nota_final = (nota1 * 0.3) + (nota2 * 0.7)

dicc = {
    "estudiante":nombre, 
    "ramo":asig, 
    "notalab1":nota1,
    "notalab2":nota2,
    "promedio":round(nota_final,1)
}

print(dicc)
