from time import sleep


def escreva(msg):
    estilo = (int(len(msg)) + 4)
    print('~' * estilo)
    print(f'  {msg}')
    print('~' * estilo)


def ajuda():
    while True:
        escreva('SISTEMA DE AJUDA PyHELP')
        sleep(1)
        comando = input('Função ou Biblioteca >')
        if comando.upper() == 'FIM':
            print('\033[31m FIM DO PROGRAMA \033[m')
            break
        escreva(f'Acessando o manual do comando {comando}')
        sleep(1)
        print('\033[34m')
        help(comando)
        print('\033[m')


ajuda()