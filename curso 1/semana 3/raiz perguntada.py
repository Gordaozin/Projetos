import math

a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
c = float(input("digite o valor de c:"))

delta = (b**2)-4 * a * c
if delta < 0:
    print("esta equação não possui raízes reais")
else:
    casoPos = (-b+math.sqrt(delta))/ (2*a)
    casoNeg = (-b-math.sqrt(delta))/ (2*a)

    if casoPos == casoNeg:
        print("a raiz desta equação é",casoPos)
    else:
        if casoPos < casoNeg:
            print("as raízes da equação são",casoPos,"e",casoNeg)
        else:
            print("as raízes da equação são",casoNeg,"e",casoPos)
