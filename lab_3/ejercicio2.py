a = [21,8,15,3,12]
b = [10,9,12,15,18]
c = [2,3,8,9,12]

#LISTA CONCATENADA
list_sum = a + b + c
print('la concatencación de las listas es ',list_sum)

#AGREGANDO 20 A LA PENULTIMA POSICIÓN

print(list_sum)

#ORDENANDO LISTA DE FORMA DESCENDIENTE
print('lista ordenada de forma descendiente')
print(sorted(list_sum))

#AGREGANDO SUMA NUEVA LISTA DE [4,5,6] EN LA ULTIMA POSICIÓN
list_sum = sorted(list_sum) + [4,5,6]
print('la lista esta ordenada con cambios en la ultima posición',list_sum)

#SUMA DE NUMEROS DE LA LISTA
list_sum = sum(list_sum)
print('la suma de todos los numeros de la lista es de: ',list_sum) 

#PROMEDIO DE LA LISTA FINAL
promedio = round(list_sum/18, 1)
print('promedio es ',promedio)