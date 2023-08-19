from datetime import date

n = int(input('Digite um ano: (digite 0 para o ano atual)'))
if n == 0:
    n = date.today().year # pega a data do computador (ano)

if n % 400 == 0:
    print(f'{n} É um ano bissexto')
else:
    if (n % 4 == 0) and (n % 100 != 0):
        print(f'{n} É um ano bissexto')
    else:
        print(f'{n} Não é um ano bissexto')


