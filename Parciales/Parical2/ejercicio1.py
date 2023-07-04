palab = str(input("Ingrese una palabra: "))

if palab[0] == palab[-1] and palab[1] == palab[-2] and palab[2] == palab[-3]:
    print('la palabra ingresasda ES un palindromo')
else:
    print('la palabra ingresada no es un palindromo')


