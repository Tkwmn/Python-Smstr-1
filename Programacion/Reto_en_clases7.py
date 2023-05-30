def txt(t):
    p = t.split()
    print(p)
    largo = len(t)
    dic = {
        'palabras':p,
        'longitud':largo
    }
    print(dic)


txt(input('escriba una frase: '))
