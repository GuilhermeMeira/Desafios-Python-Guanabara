from datetime import *
maior = 0
menor = 0

for c in range(0,7):
    ano = int(input('Digite o ano de nascimento'))
    if (date.today().year - ano) >= 21:
        maior +=1
    else:
        menor +=1

print(f'{maior} Pessoas são maiores de idade' )
print(f'{menor} Pessoas não atingiram a maioridade')
