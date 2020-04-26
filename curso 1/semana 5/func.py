#função para fatorial
def fatorial(n):
        nf = 1
        while n > 1:
            nf = nf*n
            n = n-1
        return nf

def numero_binomial(n,k):
        return fatorial(n)/ (fatorial(k)* fatorial(n-k))
