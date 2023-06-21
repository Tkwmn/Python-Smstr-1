#Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente
#parrafo

parrafo = ('''“La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional ´
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación
democratica.''').lower().split()

parrafo = tuple(parrafo)
print(f'la cantidad de veces que se repite la palabra "Universidad" es: {(parrafo.count("universidad"))} veces')




