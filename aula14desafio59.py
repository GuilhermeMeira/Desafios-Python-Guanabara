c = 0
n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
while c != 5:
    c = int(input('''O QUE DESEJA FAZER COM OS VALORES?
           [1]SOMAR
           [2]MULTIPLICAR
           [3]MAIOR
           [4]NOVOS NUMEROS
           [5]SAIR DO PROGRAMA'''))
    if c == 1:
        print(f'A soma de {n1} com {n2} é {n1 + n2}')
    elif c == 2:
        print(f'A multiplicação de {n1} com {n2} é {n1 * n2}')
    elif c == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior número entre {n2} e {n1} é {n2}')
        else:
            print('Os dois números são iguais')
    elif c == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
    elif c == 5 :
        print('Fim do programa.')
    else:
        print('Opção inválida, tente novamente!')

