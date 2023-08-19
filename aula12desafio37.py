n = int(input('QUAL NÚMERO DESEJA CONVERTER?'))
print('-' * 20)
print('DIGITE \033[36m 1 \033[m PARA BINÁRIO')
print('DIGITE \033[36m 2 \033[m PARA OCTAL')
print('DIGITE \033[36m 3 \033[m PARA HEXADECIMAL ')
print('-' * 20)
opcao = int(input('QUAL OPÇAO VOCÊ DESEJA ?'))

binary = bin(n)
octal = oct(n)
hexa = hex(n)

if opcao == 1:
    print(f'A forma binária de {n} é {binary[2:]}')
elif opcao == 2:
    print(f'A forma octal de {n} é {octal[2:]}')
elif opcao == 3:
    print(f' A forma hexadecimal de {n} é {hexa[2:]}')
else:
    print('Essa opção é inválida')
