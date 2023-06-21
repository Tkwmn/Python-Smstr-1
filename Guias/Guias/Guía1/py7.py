lista1 =  ["Martín", "Joshua", "Melanie" , "Cata", "Anfrew", "Mary"]
lista2 = [23, 34, 56, 44, 39]

diccionario = {
    "Nombres": lista1, 
    "Edad" : lista2
}

print(diccionario)

trabajadores = dict(zip(lista1,lista2))

print(trabajadores)