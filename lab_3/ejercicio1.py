dicc ={
    'id region':'los rios',
    'superficie(km^2)':'18.429',
    'habitantes (2017)': '404.43',
    'id region 2' : 'magallanes',
    'superficie(km^2) 2':'1.382.291',
    'habitantes (2017) 2': '166.533',
    }



densidad1 = round(404.432/18.429, 1)     
densidad2 = round(166.533/ 1382.291, 1) 


dicc["DENSIDAD"] = {
    'densidad region 1': densidad1,
    'densidad region 2': densidad2,
}


dicc["Capital"] = {
    'capital region 1':'valdivia',
    'capital region 2':'punta arenas'
}
print(dicc)
