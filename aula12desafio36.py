casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salário mensal?'))
anos = int(input('Em quantos anos deseja pagar?'))
meses = anos * 12
prestacao = casa/meses

if prestacao <= 0.3 * salario:
    print(f' Seu empréstimo foi APROVADO e deverá pagar {meses} parcelas de R${prestacao:.2f} ')
else:
    print(f' O seu empréstimo foi NEGADO pois a prestação mensal excede 30% do seu salário')
