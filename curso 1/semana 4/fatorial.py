n = int(input("Digite o valor n:"))
nf = n

if n==0 or n==1:
    print("1")
else:
    while n > 1:
        nf = nf*(n-1)
        n = n-1
    print(nf)
