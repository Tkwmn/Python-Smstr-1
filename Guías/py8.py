mes = str(input("ingrese un mes: ")).lower()

while mes != "enero" and "febrero" and "marzo" and "abril" and "mayo" and "junio" and "julio" and "agosto" and "septiembre" and "otubre" and "noviembre" and "diciembre":
    print("valor no coincide")
    mes = str(input("ingrese un mes: ")).lower()

if mes == "diciembre" or mes == "enero" or mes == "febrero": 
    print("el mes de ",mes," esta en verano")
else:
    if mes == "marzo" or mes == "abril" or mes == "mayo":
       print("el mes de ",mes," esta en otoño") 
    else:
        if mes == "junio" or mes == "julio" or mes == "agosto":
            print("el mes de ",mes," esta en invierno") 
        else:
            if mes == "septiembre" or mes == "otubre" or mes == "novimebre":
                print("el mes de ",mes," esta en primavera")


