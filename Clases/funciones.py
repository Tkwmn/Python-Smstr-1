#def = palabra reservada para funciones

def mi_primera_funcion():
    print('esta es mi primera funcion')

#llamar la funcion
mi_primera_funcion()

def concatenar(lista1,lista2):
    return lista1+lista2
lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()

print(concatenar(lista1,lista2))

def multiplicacion (num1, num2):
    return num1*num2

#multiplicacion
print(multiplicacion(5,5))


#ejemplo

def suma(a, b):
    return a + b 

def resta(a, b):
    return a - b 

a = int(input("ingrese un valor: "))
b= int(input("ingrese otro valor: "))

#llama a la función suma
resultado = suma(a, b)
print("la resta es de: ", resultado)


#llama a la fución resta
resultado2 = resta(a, b)
print("la resta es de ",resultado2)

