salario = float(input('Digite o seu salário: '))

if salario > 1250:
    print(f'Parabéns, voce recebeu um aumento de 10%. Seu salário agora é:{(salario*1.1):.2f}')
else:
    print(f'Parabéns, você recebeu 15% de aumento. Seu salário agora é:{(salario*1.15):.2f}')