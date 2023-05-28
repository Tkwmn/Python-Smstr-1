import random

lista =[]

for i in range(0,20):
    lista.append(random.randint(40,350))
    print('el numero al azar de la lista es: ',(lista[i]))

buscar = int(input('ingrese un numero para indicar la cantidad de concurrencias: '))

print('la cantidad de concurrencias del numero',buscar,' es de ',lista.count(buscar))

