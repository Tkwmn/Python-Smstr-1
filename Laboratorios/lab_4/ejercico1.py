Trabajador = [["Juan", [700000, 650000, 690000]], ["María", [681000, 710000, 590000]],
["Pedro", [590000, 635000, 705000]]]

def prom(sueldo):
    suma = sum(sueldo)
    promedio = suma/len(sueldo)
    return promedio

def sueld_max(sueldo):
    sueldomax = max(sueldo)
    return sueldomax

def impuest_reten(sueldomax):
    retencion = sueldomax * 0.1125
    return retencion

for i in Trabajador:
    trabajador = i[0]
    sueldo1 = i[1]
    promedio_t = prom(sueldo1)
    print("El promedio de", trabajador, " es ",promedio_t)
    print("El sueldo maximo del ", trabajador, " es de ", sueld_max(sueldo1))
    print("La retencion de impuestos del ", trabajador, " es de ", impuest_reten(sueld_max(sueldo1)))