dia = 12000
noche = 16000
domingodia = dia + 2000
domingonoche = noche + 3000
trabajadores ={
    'Trabajador 1':{
    'turnos dia':['jueves','viernes'],
    'turnos noche':['lunes','martes','miercoles']
    },
    'Trabajador 2':{
    'turnos dia':['Domingo'],
    'turnos noche':['martes','miercoles','jueves']
    },
    'Trabajador 3':{
    'turnos dia':['miercoles','jueves','viernes'],
    'turnos noche':['Sabado','Domingo']
    }
}
for i,dias in trabajadores.items():
    totalsemana = 0
    for j in dias['turnos dia']:
        if j == 'Domingo':
            pagodiario = domingodia*10
        else:
            pagodiario = dia*10
        totalsemana += pagodiario
    for k in dias['turnos noche']:
        if k == 'Domingo':
            pagodiario = domingonoche*10
        else:
            pagodiario = noche*10
        totalsemana += pagodiario

    diastrabajados=len(trabajadores[i]['turnos dia']) + len(trabajadores[i]['turnos noche'])
    trabajadores[i]['Pago diario'] = round(totalsemana/diastrabajados)
    trabajadores[i]['Total semanal'] = totalsemana

print('trabajador 1: ',trabajadores['Trabajador 1'])
print('trabajador 2: ',trabajadores['Trabajador 2'])
print('trabajador 3: ',trabajadores['Trabajador 3'])
