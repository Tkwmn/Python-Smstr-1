n1 = int(input("Indique primer numero entero: "))

n2 = int(input("Indique segundo numero entero: "))

n3 = int(input("Indique tercer numero entero: "))

if n1 and n2 < n3:
    print("el numero ",n3," es mayor")
elif n1 and n3 < n2:
    print("el numero ",n2," es mayor")
elif n2 and n3 < n1:
    print("el numero ",n1," es mayor")
else:
     print("Los numeros son iguales, por ende niguno es mayor a otro.")
    