def partida():
    n = int(input("Com quantas peças deseja começar a jogar?\n"))
    m = int(input("Qual o limite de peças por rodada?\n"))

    if (n%(m+1))==0:
        print('Voce começa!')
        condição = 0
    else:
        print('Computador começa!')
        condição = 1

    if condição == 0:
        while n>0:
            n = usuario_escolhe_jogada(n,m)
            n = computador_escolhe_jogada(n,m)
            if n==0:
                break

    if condição == 1:
        while n>0:
            n = computador_escolhe_jogada(n,m)
            if n==0:
                break
            n= usuario_escolhe_jogada(n,m)

def computador_escolhe_jogada(n,m):
    b = n
    if n < (m + 1):
        num_comp = n
    else:
        num_comp = (n % (m + 1))
    n = b - num_comp
    if n == 0:
        print("O computador tirou",num_comp,"peças,"," não restam peças no tabuleiro")
        print("Fim do jogo! O computador ganhou!")
    else:
        print ("O computador tirou",num_comp,"peças","restam",n,"no tabuleiro")
    return n



def usuario_escolhe_jogada(n,m):
    num_jog = int(input("Quantas peças você vai tirar?\n"))
    y = num_jog
    while y<=0 or y>m:
        num_jog = int(input("Oops! Jogada inválida! Tente de novo."))
    n = n - num_jog
    print ("você removeu",num_jog,"peças","restam",n,"no tabuleiro")
    return n

print("Olá, bem vindo ao NIM\nVamos começar?")
print("1 - para jogar uma partida isolada.")
print("2 - para jogar um campeonato.")
escolha = int(input())

if escolha == 1:
    print("Você escolheu uma partida isolada.")
    partida()
    print('***** Final da partida! ******')
    print('Placar: Você 0 x 1 Computador')
if escolha == 2:
    print("Você escolheu um campeonato.")
    partid = 1
    while partid<4:
        print(' **** Rodada',partid, '*****')
        partida()
        partid = partid + 1
    print('***** Final do Campeonato! ******')
    print('Placar: Você 0 x 3 Computador')
