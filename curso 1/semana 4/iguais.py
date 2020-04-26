a = int(input("digite um número inteiro:"))
igual = False
while a>0:
    b = a%10
    a = a//10
    c = a%10
    if b==c:
        igual = True

if igual:
    print("sim")
else:
    print("não")
