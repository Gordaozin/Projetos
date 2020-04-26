#equação pelas raízes
x1 = float(input("Digite a primeira raiz"))
x2 = float(input("Digite a segunda raiz"))

a = int(-(x1+x2))
b = int(x1*x2)

if a>0 and b>0:
    print("x²+",a,"+",b)
if a>0 and b==0:
    print("x²+",a,)
if a<0 and b>0:
    print("x²",a,"x","+",b)
if a<0 and b<0:
    print("x²",a,b)
