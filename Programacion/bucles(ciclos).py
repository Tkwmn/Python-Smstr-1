num = 0

while num <= 100:
    print(num)
    num += 2
print('primer bucle terminado')

#bucle infinito

#edad = 19

#while edad > 18:
    #print("eres mayor de edad")
#while true:
    #print(num)
    #num+= 2

# ¿que hace este bucle?

print("\nimpresion de numeros de 0 al 100(incrementado de 2 en 2)")
num = 0

while num <= 100:
    print(num)
    num += 2
    #num = num + 2
print('segundo bucle terminado')

#combinando while y if

print("\nimpresion de numeros de 200 al 300(incrementando de 2 en 2) + if en 250")

while num <= 300:
    print(num)
    num += 2
    if num == 250:  
        print("mi   condición es igual a 250")
print("tercer bucle terminado\n")

#utilizanod break

print("\nimmpresion de numeros de 300 al 400(incrementando de 2 en 2) + break en 350")

while num <= 400:
    print(num)
    num += 2
    if num == 350:
        print("se detiene la ejecución")
        break
print(num)
print("cuarto bucle terminadoo\n")

#utilizando continue
print("\nimpresión de numeros de 0 al 50 (Incrementando de 1 en 1) + continue if == 40")
num = 0

while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)


#Loop infinito + break
# while True:
#     parametro = input(">")
#     if parametro == "exit":
#         break
#     else:
#         print(parametro)

#FOR

print("\n   impresion de una lista de 10 elementos de forma vertical (utilizando for)")
print("\n for n°1")

#no bien optimizado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(1)

print("\n for n°2")
nuevalista = [1,2,3,4,5,6,7,8,9,10]
for i in nuevalista:
    print(i)

print("\n for n°3")
for i in (1,11):
    print(i)

# iterador e iterables

print("iterador o iterables")
iterador = iter(nuevalista)

print(next(iterador))  #imprime 1
print(next(iterador))  #imprime 2
print(next(iterador))  #imprime 3
print(next(iterador))  #mprime 4
print(next(iterador))  #imprime 5 y así

print(iterador)