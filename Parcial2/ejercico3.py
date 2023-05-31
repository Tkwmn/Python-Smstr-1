t_mi = {9,5,2,7,6,1}
t_ma = {12,14,11,10,15,9}
print("\n")
print('Temperaturas minimas: ',t_mi)
print('Temperaturas maximas: ',t_ma)
print("\n")

#A)Verificar si la temperatura 9°C está en ambos sets

print("VERIFICAR SI LA TEMPERATURA 9°C ESTÁ EN AMBOS SETS")
if 9 in t_mi and 9 in t_ma:
    print('La temperatura 9° si está en niguno de los 2 sets')
else:
    print('La temperatura 9° no está en niguno de los 2 sets')
print("\n")

T =(int(input("Ingrese algun numero para verificar si esta o no en ambas tablas de T°: ")))

if T in t_mi and T in t_ma:
    print('La temperatura ', T,'° si está en los 2 sets')
else:
    print('La temperatura ', T,'° no está en AMBOS sets')
print("\n")

#B)Comprobar si al menos la temperatura 6°C y 17°C está en alguno de los sets

if 6 in t_mi or 6 in t_ma:
    print("La temperatura 6° solo está en un set")
else:
    print("La temperatura 6° no está en ninguno de los sets")

if 17 in t_mi or 17 in t_ma:
    print("La temperatura 17° solo está en un set")
else:
    print("La temperatura 17° no está en ninguno de los sets")
print("\n")

T2 = int(input('COMPRUEBE SI ALGUNA T° SE ENCUENTRA EN UNO DE LOS SETS: '))

if T2 in t_mi and T2 in t_ma:
        print("La temperatura",T2,"° está en ambos set")
elif T2 in t_mi or T2 in t_ma:
    print("La temperatura",T2,"° solo está en un set")
else:
    print("La temperatura",T2,"°no está en ninguno de los sets")
print("\n")

#C)Elevar a 4 todas las temperaturas dentro de los sets

print("ELEVAR A 4 TODAS LAS TEMPERATUAS DENTRO DE LOS SETS")
t_mi2 = {9**4,5**4,2**4,7**4,6**4,1**4}
print('Temperaturas minimas^4: ',t_mi2)
t_ma2 = {12**4,14**4,11**4,10**4,15**4,9**4}
print('Temperaturas maximas^4: ',t_ma2)
print("\n")

#D)Unir ambos sets en uno solo

t_mi2.update(t_ma2)

print('la unión de ambos sets es ',t_mi2)


