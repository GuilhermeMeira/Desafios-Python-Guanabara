n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print(f'Sua média é: {media:.2f} e você foi REPROVADO.')
elif 5 < media < 7:
    print(f' Sua média é {media:.2f} e você está de RECUPERAÇÃO.')
else:
    print(f'Parabéns, você foi APROVADO com média {media:.2f}')

