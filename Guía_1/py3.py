a = float(input("cuanto mide el primer lado del triangulo?: "))
b = float(input("el segundo lado cuanto mide?: "))
c = float(input("cuanto mide el ulitmo lado?: "))

if a == b == c:
    print("el triangulo es equilatero")
else:
    if a != b != c:
        print("el triangulo es escaleno")
    else:
        if a or b == c:
            print("el triangulo es isosceles")

perim = (a + b + c)/2

area = round((perim * (perim-a) * (perim-b) * (perim-c))**0.5)

print("y el area del triagulo es ",area)
