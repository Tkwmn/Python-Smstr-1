a = [10,80,15,30,20]
b = [20,45,80,20,10]
c = [20,35,60,90,20]
def valores_comun(a ,b, c):
    comu = []
    for i in a:
        if i in b and c:
            comu.append(i)
    return comu

def eliminar_duplicados(lista):
    lista = list(set(lista))
    return lista

def concatenar(a, b, c):
    lista = a + b + c
    return lista

def ord_descendente(lista):
    lista_ordenada = lista.sort(reverse = True)
    return lista_ordenada

def reemplazar_posicion7(lista):
    num = lista[6]
    lista.insert(num, 100)
    return lista


print("Los valores comunes entre a, b y c son: ", valores_comun(a, b, c))
listas = concatenar(a, b, c)
print("Listas concatenadas ", listas)
ord_descendente(listas)
print("Lista ordenada en descendente", listas)
reemplazar_posicion7(listas)
print("La lista con el valor de la posicion 7 reemplazado: ",listas)