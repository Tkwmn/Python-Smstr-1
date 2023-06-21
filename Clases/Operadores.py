a = 20
b = 5
c = 4
d = 20

print("la suma entre a + b es:", a + b)
print("la resta entre a - b es:", a - b )
print()

x = 2 + 3
print(x)

y = 7 - 4
print(y)

z = 5 * 6
print(z)

f = 10 / 2
print(f)

g = 10 // 3
print(g)

h = 2 ** 3
print(h)

o = 7 % 3
print(o)

#declarando variables de tipo flotantes 

tiempo = 5.39
gravedad = 9.81

#operaciones aritmeticas con flotantes 
velocidad = tiempo * gravedad

print("la velociad en caida libre del objeto es de ", velocidad, "m/s")
print("la velociad en caida libre del objeto es de ",velocidad,"m/s")

#variables de tipo complejo 
c1 = 4 + 3j
print(type(c1))

#creando n° complejo con complex
c2 = complex(4, -6)
print("el numero complejo es ",c2)

print(c2.real) #obtener la parte real de numero complejo 
print(c2.imag) #obtener la parte imaginaria del numero

#¿se puede multiplicar un str por un entero?
print("hola" * 5)

#¿y esta?
"""print("hola" * 3.5 * 2)""" #No, nos pasamos poniendo enteros, flotantes y string

#¿y esta otra?
print("hola" * (int((10 * 2)/ 5)),"\n") #si, ya que es un n° entero y no hay flotantes

#¿y esta?
#print("hola" + 20)

print("hola" + str(20))

"""########### 02-OPERADORES DE COMPARACION ##########"""

#comparando terminos numericos

print("comparando numeros")
print(a == b)
print(a != b)
print( a > b)
print(a < b)
print(c >= d)
print(c <= d)

#comparando cadena de texto(caracteres)

animal_domesticado = "gato"
animal_salvaje = "leopardo"

print("\ncomparando cadenas de texto(caracteres)")
print(animal_domesticado == animal_salvaje)
print(animal_domesticado != animal_salvaje)
print(animal_domesticado > animal_salvaje)
print(animal_domesticado < animal_salvaje)
print(animal_salvaje >= animal_domesticado)
print(animal_salvaje <= animal_domesticado)

#operadores logicos

bencina = True
encendido = True
edad = 19

print(bool(bencina))
print(bool(not bencina)) #Se transforma en False, y si fuera False se transformaria en True


#utiliando operar 'and'
if bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el veiculo no puede arrancar")

#utilizando operador 'or'

if bencina or encendido:
    print("el vehiculo puede avanzar")
else:
    print("el veiculo no puede arrancar")

#utilizando operador 'not' y 'and'
if not bencina and encendido:
    print("el vehiculo puede avanzar")
else:
    print("el vehiculonno puede arrancar")

#utilizando operador 'not' y 'or'
if not bencina or encendido:
    print("Utilizando NOT Y OR:  El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#utilizando los operadores 'not', 'or' y 'and'
if not bencina or (encendido and edad >= 18):
    print("el vehiculo puede avanzar")
else:
    print("el vehiculo no puede arrancar")

