def main():
    a = int(input("digite um numero inteiro:"))
    maior_primo(a)

def ehPrimo(n):
    total_div = 0
    for divisores in range (1, n + 1):
        if n % divisores == 0:
            total_div = total_div + 1
    if total_div == 2:
        return True
    else:
        return False


def maior_primo(k):
    a = k
    while ehPrimo(k)== False:
        k = k-1
    print("o maior numero primo dentro de",a,"é",k)
main()
