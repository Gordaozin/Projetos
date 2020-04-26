digitoIgual =  False

a = int(input("digite:"))

while a > 0:
    b = a % (10)
    a = a // (10)
    c = a % 10
    print(a,b,c)
    if c == b:
        digitoIgual = True

if digitoIgual == True:
    print("boa garoto")
else:
    print('denovo não')
