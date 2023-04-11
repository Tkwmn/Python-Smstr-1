# Datos de un tipo numerico

edad = 29 #entero
estatura = 1.71 #real
peso = 70 #real
complejo = 1+4j #se pone j para los complejos
print("######## 01- datos numericos ########");
print("impresion de un numero complejo",complejo,'\n')
print(f"mi estatura es de {estatura}")

# Operaciones artimetica basica para sacar el imc

imc = peso/estatura**2
print("Mi IMC es de:",imc)

#el codigo {:..2f} es para aproximar y va entre comillas y .format es para 

print("mi IMC es de: {:..2f}".format(imc), '\n')

# Datos de tipo cadena de caracteres

asignatura = 'programación'
carrera = 'Ingenieria Civil en Informatica'
print("######### 02-STRINGS ########")
print('La asignatura de',asignatura,'corresponde a la carrera de',carrera)
print("la cantidad de caracteres de la palabra", asignatura)


# Valores booleanos

ampolleta = False
interruptor= True


# Con type sabemos el tipo de datos  que estamos tratamdo

print(type(ampolleta))

# Datos tipo array (objetos de tipo colección)
estudiantes = ['Nicolas', 'Israel', 'Melany', 'Darly']
num = [1,2,3,4,5,6]
lenguaje = ("Python")


#¿Se puede realizar una lista de datos compuestos?

print(estudiantes)



