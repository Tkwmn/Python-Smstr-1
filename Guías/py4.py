nombre1 = str(input("Ingrese su nombre: "))
nombre2 = str(input("Ingrese otro nombre: "))

if nombre1[0] == nombre2[0]:
    print("los mombres inician con lo misma letra")
else:
    if nombre1[-1] == nombre2[-1]:
     print("los nombres finalinzan con la misma letra")
    else:
       print("los nombres no inician ni finalizan con la misma letra")
