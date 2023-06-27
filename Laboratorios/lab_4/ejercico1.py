Trabajador = [["Juan", [700000, 650000, 690000]], ["María", [681000, 710000, 590000]],
["Pedro", [590000, 635000, 705000]]]

def promedio(sueldo):
    suma = sum(sueldo)
    promedio = suma/len(sueldo)
    return promedio

def sueldomaximo(sueldo):
    sueldomax = max(sueldo)
    return sueldomax

def retencion_impuesto(sueldomax):
    retencion = sueldomax * 0.1125
    return retencion

for i in Trabajador:
    trabajador = i[0]
    sueldos = i[1]
    promedio_t = promedio(sueldos)
    print("El promedio de",trabajador," es ",promedio_t)
    print("El sueldo maximo del ",trabajador," es de ",sueldomaximo(sueldos))
    print("La retencion de impuestos del ",trabajador," es de ", retencion_impuesto(sueldomaximo(sueldos)))