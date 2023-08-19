def leiaint(msg):
    while True:
        try:
            x = int(input(msg))
        except (ValueError, TypeError):
            print(f'ERRO DE TIPO OU VALOR, TENTE NOVAMENTE')
        except KeyboardInterrupt:
            print()
            print('O usuário preferiu não digitar esse número')
            x = 0
            return x
        else:
            return x


def leiafloat(msg):
    while True:
        try:
            x = float(input(msg))
        except(ValueError, TypeError):
            print(f'ERRO DE TIPO OU VALOR, TENTE NOVAMENTE')
        except KeyboardInterrupt:
            print()
            print('O usuário preferiu não digitar esse número')
            x = 0
            return x
        else:
            return x


a = leiaint("Digite um número")
b = leiafloat("Digite um número real")
print(f'O INTEIRO É {a} E O REAL É {b}, A SOMA DA {a + b}')
