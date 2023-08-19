import random
jogos = []
jogada = []
cont = 0
quantos = int(input("Quantos jogos quer fazer?"))
for x in range(0, quantos):
    for i in range(0, 6):
        jogo = random.randint(1, 60)
        if jogo in jogada:
            while jogo in jogada:
                jogo = random.randint(1, 60)
            jogada.append(jogo)
        else:
            jogada.append(jogo)
    cont += 1
    jogos.append(jogada[:])
    jogada.clear()
    print(f'Jogo {cont}: {jogos[x]}')
