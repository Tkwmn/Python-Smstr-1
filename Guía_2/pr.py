def calcular_cubos(n):
    cubos = []
    suma_impares = 1  # Primer impar
    for i in range(n):
        cubo = suma_impares ** 3
        cubos.append(cubo)
        suma_impares += 2  # Siguiente impar
    return cubos

# Obtener el valor de n desde el usuario
n = int(input("Ingrese el valor de n: "))

# Calcular y mostrar los primeros n cubos
cubos = calcular_cubos(n)
for i, cubo in enumerate(cubos):
    print(f"{i+1} => {cubo}")
