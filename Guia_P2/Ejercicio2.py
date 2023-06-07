# Utilizar una funcion que permita ingresar nombres para que el usuario ingrese nombres ´
# uno por uno. Los nombres se deben almacenar en una lista

nombres=[]
while True:
    n = str(input("Ingrese nombres (Escriba 'Terminar' para terminar): "))
    nn = n.replace(" ","")
    if nn.lower() != "terminar":
        print(nn)
        nombres.append(nn)
    else:
        print("INGRESO DE NOMBRES FINALIZADO")
        break   

# Luego, crear otra funcion
# que permita contar las letras, la cual debe recorrer la lista de nombres y cuente
# la cantidad total de letras de todos los nombres ingresados

def cantidadletras(nombres):
    letrastotal = 0
    for nombre in nombres:
        letrastotal += len(nombre)
    return(letrastotal)

letrastotal = cantidadletras(nombres)

print("Los nombres ingresados son ",nombres," y las letras totales son ",letrastotal)