lista1 = [4,3,8,12,6,10,14,3,6]
print("la lista esta compuesta de: ",lista1)

lista1.pop(-1)
print("la lista se modificó, ahora se compone de: ",lista1)

lista1.insert(0,2)
print("la lista se modificó, se ahora se compone de: ",lista1)

lista1 = list(set(lista1))
print("la lista se modificó, se eliminaron numeros repetidos, ahora se compone de: ",lista1)

#(--------------------------------------------)#

lista1 = [4,3,8,12,6,10,14,3,6]

cantidad = len(lista1)
suma = sum(lista1)
media = round((suma/cantidad), 1)

#--------mediana-------#

lista1.sort()
mediana_index = (cantidad//2)

if (cantidad/2) == 0.5:
    mediana = lista1[mediana_index]
else:
    mediana1 = lista1[mediana_index -1]
    mediana2 = lista1[mediana_index]
    mediana = (mediana1+mediana2)/2

print('lista ordendada',lista1,' y la media es de ',media, " con valor de mediana como ", mediana)
