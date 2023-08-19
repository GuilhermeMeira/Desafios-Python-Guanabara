import random
from time import sleep
from operator import itemgetter
pontos = []
jogo = {'Jogador 1 ': random.randint(1, 6),
        'Jogador 2 ': random.randint(1, 6),
        'Jogador 3 ': random.randint(1, 6),
        'Jogador 4 ': random.randint(1, 6)}

for k, v in jogo.items():
    print(f' {k} tirou {v}')
    sleep(0.1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for p, dado in enumerate(ranking):
    print(f'{p + 1} lugar : {dado[0]} com {dado[1]} pontos')


