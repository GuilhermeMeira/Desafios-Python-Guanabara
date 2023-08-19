import random
import time
jogadas = ['Pedra', 'Papel', 'Tesoura']
print('-' * 35)
print('PEDRA PAPEL E TESOURA')
print('-' * 35)

jogada = (input('Escolha a sua jogada:')).capitalize()
jogadapc = random.choice(jogadas)

print(f'\033[1;36mVocê escolheu \033[1;35m{jogada}\033[m')
print('\033[1;36mProcessando...')
time.sleep(2)
print(f'O computador escolheu \033[1;35m{jogadapc}\033[m')

if jogada == 'Pedra' and jogadapc == 'Papel' \
        or jogada == 'Papel' and jogadapc == 'Tesoura' \
        or jogada == 'Tesoura' and jogadapc == 'Pedra':
    print('\033[1;31mVocê PERDEU ')

elif jogada == 'Pedra' and jogadapc == 'Tesoura' \
        or jogada == 'Papel' and jogadapc == 'Pedra' \
        or jogada == 'Tesoura' and jogadapc == 'Papel':
    print('\033[1;32mVocê VENCEU')

elif jogada != 'Pedra' and jogada != 'Papel' and jogada != 'Tesoura':
    print(f'\033[4;37m{jogada} Não é válido :(')
else:
    print('\033[1;33mVocê EMPATOU!')


