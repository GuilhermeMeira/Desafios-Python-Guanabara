import datetime
ano = int(input('Digite o seu ano de nascimento: '))
idade = datetime.date.today().year - ano

if idade < 18:
    print(f'Você vai se alistar daqui a {18 - idade} anos.')
    print(f'O seu alistamento será em: {(18 - idade) + datetime.date.today().year }')
elif idade > 18:
    print(f'Você ja se alistou ou está atrasado há {idade - 18} anos.')
    print(f'Seu alistamento deveria ter sido em {  datetime.date.today().year - (idade - 18) }')
else:
    print('Você deve se alistar esse ano !')