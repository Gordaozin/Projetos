def ehPrimo(n):
    total_div = 0
    for divisores in range (1, n + 1):
        if n % divisores == 0:
            total_div = total_div + 1
    if total_div == 2:
        return True
    else:
        return False

def n_primos():
    a = int(input("digite um numero inteiro:"))
    soma = 0
    while a >=2:
        if ehPrimo(a) == True:
            soma = soma + 1
        a = a - 1
    print(soma)

n_primos()
