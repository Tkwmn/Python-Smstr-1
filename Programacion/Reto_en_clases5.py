n = int(input('ingrese numero: '))
i = 1

while n < 1:
   n = int(input('porfavor ingrese un numero valido: '))

if n % 2 == 0:
   print('el numero es par')
else:
   print('el numero es impar')

suma=1
while i<n:
   if n%i==0:
      suma+=1

if suma == 1:
   print('el numero es primo')
else:
   print('no es primo')

if n > 50:
   print('el numero es mayor a 50')
else:
   print('el numero es menor a 50')


