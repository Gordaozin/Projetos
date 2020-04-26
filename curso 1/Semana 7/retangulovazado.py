
l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

largura = 0
altura = 0

while altura < a:
    if altura > 0 and altura < a-1 :
        while largura < l:
            if largura == 0 or largura == l-1:
                print("#",end="")
            else:
                print(" ",end="")
            largura = largura + 1
    else:
        while largura < l:
            print('#',end="")
            largura = largura + 1
    altura = altura + 1
    largura = 0
    print()
