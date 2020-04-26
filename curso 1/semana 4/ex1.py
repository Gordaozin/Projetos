a = int(input("Digite um número inteiro:"))
soma = 0

while a > 0:
    b = a % 10
    a = a//10
    soma = soma + b
print(soma)
