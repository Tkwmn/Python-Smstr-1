lista1 = [4,3,8,12,6,10,14,3,6]

print("la lista esta compuesta de: ",lista1)

del lista1[-1]

print("la lista se modificó, ahora se compone de: ",lista1)

lista1.insert(0,2)

print("la lista se modificó, ahora se compone de: ",lista1)

for i in lista1:
    if lista1.count(i) > 1:
        lista1.remove(i)

print("la lista se modificó, ahora se compone de: ",lista1)

media = round(sum(lista1)/len(lista1), 1)

lista_ordenada = sorted(lista1) 

posicion = round((len(lista1)/2) -1)

mediana = lista_ordenada[posicion]

print("la lista ordenada es ",lista_ordenada," y la media es de ",media,", con mediana de ",mediana)