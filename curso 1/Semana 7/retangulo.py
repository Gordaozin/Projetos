
l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))

largura = 0
altura = 0

while altura < a:
    while largura < l:
        print('#',end="")
        largura = largura + 1
    altura = altura + 1
    largura = 0
    print()
