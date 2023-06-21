# Datos de un tipo numerico

edad = 29 #entero
estatura = 1.71 #real
peso = 70.5 #real
complejo = 1+4j #se pone j para los complejos
print("impresion de un numero complejo",complejo,'\n')
print(f"mi estatura es de {estatura}")

# Operaciones artimetica basica para sacar el imc

imc = peso/estatura**2

#transformando Real a Entero
print(peso)
print("transformando un valor Real a Entero:",int(peso))

print(edad)
print("transformando Entero a Real:",float(edad))
print("Mi IMC es de:",imc)

#el codigo {:..2f} es para aproximar y va entre comillas y .format es para 

print("mi IMC es de: {:.2f}".format(imc), '\n')


# Datos de tipo cadena de caracteres

asignatura = 'programación'
carrera = 'Ingenieria Civil en Informatica'
print("######### 02-STRINGS ########")
print('La asignatura de',asignatura,'corresponde a la carrera de',carrera)
print("la cantidad de",len(asignatura), "corresponde a la carrera de ",len(carrera))


# Valores booleanos

ampolleta = False
interruptor= True


# Con type sabemos el tipo de datos  que estamos tratamdo

print(type(ampolleta),"\n")
ampolleta = "soy una ampolleta"
print(type(ampolleta),"\n")

#podemos transformar cualquier valor a un booleano (al igual que un string)
print(bool(0)) #0 significa apagado por lo que es false 
print(bool("")) #vacío por lo que dará false
print(bool(None)) #ninguno por lo que dará false
print(bool("False")) #es una cadena de texto por lo que es True
print(bool(1)) #1 es encendido por lo que siemore va a dar true
print("\n")

# Datos tipo array (objetos de tipo colección)
estudiantes =['Nicolas', 'Israel', 'Melany', 'Darly']
num =[1,2,3,4,5,6]
lenguaje =("Python")
data = ["osorno", {"UV": "nivel bajo", "Temp °C":15}, (-40.5725, -70.432)]
print(data)
print(len(data)) #Con len() podemos ver cuantos tipos de elementos, hay , deberian ser 3
print("lista de cadena de caracteres:", estudiantes)
print("lista de numeros:", num)
print("lista de elementos:", lenguaje)

listamixta = [100, "Felipe", False]
print(len(listamixta)) #Para ver cuantos elementos hay en una lista 

#con .count() podemos bucar un elemento de la lista
#que es una colewccion ordenada, los elementos de la lista y nos muestra donde está

print(estudiantes.count(int("Israel")))

#datos tipo array (objetos de tipo coleccion) o arreglos. con erray se gasta menos memoria que con list() pero lis() es mas dinamico
#y array es mas limitado a un tipo de dato

nueva_lista = list(11,13,14,12)
nueva_listita = [10,11,12]
print("esta es una lista vacia", nueva_lista,"\n")


#los corchetes [] se utilizan para crear una lista 
#que es una coleccion ordenada, los elementos de la lista estan separados por comas

#como acceder a un elemento especifico en la lista?

print(estudiantes[0])
print(estudiantes[1])

#reasignar el valor de una posición 

estudiantes[0] = "gabriela"

print(estudiantes[0],"\n")

#inicializando otra lista de datos mixtos

data_asig = [10023, "programacion", 1, True]

#¿que hace este codigo?

cod, ramo, semestre, estado = data_asig
print(ramo, "\n")


#que hacen estas funcionies?

print(list("python"))
print(list(range(10)))
print("\n")

#TUPLAS, las tuplas se hacen con parentesis y no son mutables


grupo1 = ("Alvaro", "Liliana", "Felipe", 200, 100, "Alvaro")
print("##### TUPLAS #####")
print(type(grupo1),"\n")

#accediendo al primer alemento de la tupla

print(grupo1[0])
#consultando el elemento "alvaro" cuantas veces se encuentra en la tupla

print("el elemento se repite:",grupo1.index("alvaro"), "\n")

#reasignar el primer elemento de la tupla
#grupo1[0]="costanza"
#print(grupo1[0])
#NO ES MUTABLE 

#se pueden sumar las tuplas?
grupo2 = ("costanza", "Aron", 150, 250)
grupos = grupo1 + grupo2
print(grupos,"\n")

#Entonces como no puedo modificar una tupla,¿Que puedo hacer?
grupo1 = list(grupo1)

print("la tupla ahora es de tipo",type(grupo1),"\n")
print("\n")
print(grupo1[1:4])

#SETS o conjuntos
#Formas de inicializar un Set 

conjunto_vacio = set()
conjunto_vacio1 = {} #¿diccionario o set?
print(type(conjunto_vacio)) 

conjunto_colores = set({"azul", "rojo", "verde"})   #utilizar funcion set
conujunto_animales = {"gato","perro","loro"} #utilzar corchetes
print(type(conjunto_colores))
print(type(conujunto_animales)) #es un set por que se añadieron elementos, aunque se haya hecho con llaves
print("el primer set contiene los colores: ",conjunto_colores)
print("el segundo set contiene los siguientes animales: ",conujunto_animales)

#print(conjuntos_animales[0]) #accediendo al primer elemento del set(dará error).
conjunto_colores.add("violeta")
print("el set de colores se conforma por: ",conjunto_colores)
conujunto_animales.add("lechuza")
print("el set de animales esta compuesto por: ",conujunto_animales)
print("\n")

"""-----Diccionarios-----"""

diccionario1 = dict()
diccionario2 = {}

print(type(diccionario2))

datos_personales ={
    "nombre":"melany",
    "institución":"ulagos",
    "edad":"18",
    "asigntauras": {"estructura de datos","programación"}
    }

print("diccionario inicial: ",datos_personales)

#clave es lo mismo que un campo
#consulta la cantidad de elementos del diccionario

print(len(datos_personales))

#como acceder a un elemento especifico de un lista?
print(datos_personales["Institución"])

#actualizar el valor de una clave dentor de un diccionario?

datos_personales["institución"] = "USS"

#agregando un nuevo campo al diccionario

datos_personales["ciudad"] = "osorno"
print(datos_personales)

#eliminando un campo del dicciinario

del datos_personales["ciudad"]
print("diccionario con in campo eliminado: ",datos_personales)

hospital = dict(
    nombre = "hospital san tomas",
    direccion = "dr. guillermo buhler 1765",
    ciudad = "osorno"
    )
