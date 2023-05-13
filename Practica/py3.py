letra1 = str(input("Escriba alguna palabra: "))
letra2 = str(input("Escriba otra palabra: "))

if len(letra1) < len(letra2):
    print(letra1," tiene menos letras")
    print(letra2," tiene mas letras")
else:
    print(letra1," tiene mas letras")
    print(letra2," tiene menos letras")
    