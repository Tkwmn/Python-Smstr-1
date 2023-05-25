suma = 0
for i in range(500,801,10):
    suma+= i
    print(suma)
    for j in range(456,i==800,-2):
        suma += j
        print(suma)
print(f'la suma es de ',{suma})