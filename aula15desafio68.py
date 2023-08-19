import random
import time
lista = ["par","impar"]
contv = 0 #contador de vitórias

while True:
    jogada = int(input('Digite um número'))
    jogadapc = random.randint(0, 10)
    jogada2 = input('Par ou impar?').upper().strip()
    soma = jogada + jogadapc
    if jogada2 == 'PAR':
        jogadapc2 = 'IMPAR'
    else:
        jogadapc2 = 'PAR'
    print('-' * 50)
    print(f'Você jogou {jogada2} e o computador jogou {jogadapc2}')
    print('-' * 50)
    time.sleep(2)
    if soma % 2 == 0: #se o número for par
        if jogada2 == 'PAR' and jogadapc2 == 'IMPAR':
            print(f'Você jogou {jogada} e o computador jogou {jogadapc}. O total foi {soma}, deu PAR ')
            print('PARABÉNS, VOCÊ GANHOU ! + 1 PARTIDA')
            print('-' * 50)
            contv += 1
        elif jogada2 == 'IMPAR' and jogadapc2 == 'PAR':
            print(f'Você jogou {jogada} e o computador jogou {jogadapc}. O total foi {soma}, deu PAR')
            print('Que pena, você PERDEU')
            print('-' * 50)
            break
    elif soma % 2 == 1:
        if jogada2 == 'IMPAR' and jogadapc2 == 'PAR':
            print(f'Você jogou {jogada} e o computador jogou {jogadapc}. O total foi {soma}, deu IMPAR')
            print('PARABÉNS, VOCÊ GANHOU ! + 1 PARTIDA')
            print('-' * 50)
            contv +=1
        elif jogada2 == 'PAR' and jogadapc2 == 'IMPAR':
            print('-' * 50)
            print(f'Você jogou {jogada} e o computador jogou {jogadapc}. O total foi {soma}, deu IMPAR')
            print('Que pena, você PERDEU')
            print('-' * 50)
            break
print(f'Parabéns, você venceu {contv} vezes.')