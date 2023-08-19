print(f'{"Loja do gui":^40}')
valor = float(input('Digite o valor da compra: '))

print('Digite\033[36m 1 \033[m para pagar a vista (dinheiro) com DESCONTO de 10%')
print('Digite\033[36m 2 \033[m para pagar a vista (cartão) com DESCONTO de 5%')
print('Digite\033[36m 3 \033[m para dividir em 2x no cartão sem juros')
print('Digite\033[36m 4 \033[m para dividir em 3x no cartão com juros de 20%')

opcao = int(input('Qual opção você deseja? '))

if opcao == 1:
    print(f'Você escolheu a opção 1 e pagará R${valor - (valor * 10/100):.2f}')
elif opcao == 2:
    print(f'Você escolheu a opção 2 e pagará R${valor - (valor * 5/100):.2f}')
elif opcao == 3:
    print(f'Você escolheu a opção 3 e pagará 2 parcelas de R${valor/2:.2f} totalizando R${valor:.2f}')
elif opcao == 4:
    n = int(input('Quantas parcelas você deseja?'))
    if n > 3:
        print(f'Você escolheu a opção 4 e pagará {n} parcelas de R${(valor/n) +(valor * 20/100)/n:.2f} totalizando R${valor +(valor * 20/100):.2f}')
    else:
        print('MÍNIMO DE 3 PARCELAS NESSA OPÇÃO')
else:
    print('Digite uma opção válida (1 - 4)')
