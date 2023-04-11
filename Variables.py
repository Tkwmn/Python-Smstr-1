#Declarando variables de tipo texto

print("hola soy Nicolas")

nombre = "Nicolas"
name = "Matias"


print(nombre)
print("hola soy",nombre)

#Variables de tipo numerico

edad = 18

print("mi edad es de",edad)

print("hola mi nombre es" " " + nombre + " "  "y tengo" + str(edad) +  "años de edad")

#no se puede concadenar diferentes tipos de datos +, por lo que se trasforma el dato de edad a string.
#es recomendable utilizar el signo + para unirlos, y a diferencia de la coma, no agrega espacios por lo que hay que añadirlos

print(f"hola mi nombre es {nombre} y tengo{edad} años de edad")

#desde las ultimas versiones de python se puede usar los corchetes {} para poner las variables y asi hacerlon mas amigable
nombre1 = "Yessi"

#se asigna nuevamente la variable nombre pero tambien se puede crear otra con nombre1 si es necesario tener ambas

print ("Hola mi nuevo nombre es:", nombre1)

#se usa input para pedir datos

nombre1 = input("¿Cual es tu nombre?: \n")

print("su nombre es:",nombre1) 

#el \n sirve para bajar una linea
#el identificador de una variable es un nombre

ciudad, region, pais, year = "puerto montt", "los lagos", "chile", 2023

#se puede asignar varias variables a la vez, separandolas por comas

print(f"hola vivo en {ciudad}, en la region {region}, en el pais de {pais}, y es el año {year}")
 