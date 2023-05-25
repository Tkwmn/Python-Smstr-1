mes = str(input("ingrese un mes: ")).lower()

while mes != "enero" and mes !="febrero" and mes != "marzo" and mes != "abril" and mes != "mayo" and mes != "junio" and mes != "julio" and mes != "agosto" and mes != "septiembre" and mes != "otubre" and mes != "noviembre" and mes != "diciembre":
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


