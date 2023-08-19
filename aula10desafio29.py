km = float(input('Qual a velocidade do carro em km/h?'))
multa = (km - 80) * 7

print('=' * 70)

if km > 80:
    print('\033[1;31mVOCÊ FOI MULTADO POR ULTRAPASSAR O LIMITE DE VELOCIDADE\033[m')
    print(f'\033[33mA sua multa é de\033[31m R$ {multa:.2f}')
else: print('\033[1;32mPARABÉNS, VOCÊ NÃO ULTRAPASSOU O LIMITE DE VELOCIDADE')