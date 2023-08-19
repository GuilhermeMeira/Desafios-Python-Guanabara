pessoas = {}
lista = []
soma = cont = 0
mulheres = []
acima = []
while True:
    pessoas['nome'] = input("Nome:")
    while True:
        pessoas['sexo'] = input("Sexo: M/F").upper()
        if pessoas['sexo'] not in 'MF':
            print('Sexo inválido, tente novamente.')
        else:
            break
    pessoas['idade'] = int(input("Idade:"))
    lista.append(pessoas.copy())
    cont += 1
    continuar = input('Deseja Continuar? S/N')
    if continuar.upper() == 'N':
        break
for pessoas in lista:
    soma += pessoas['idade']
for pessoas in lista:
    if pessoas['sexo'] == 'F':
        mulheres.append(pessoas['nome'])
    if pessoas['idade'] > soma/cont:
        acima.append(pessoas['nome'])
        print(acima)
print(f'{cont} Pessoas foram cadastradas')
print(f'A média de idade do grupo é: {soma/cont:.2f} ')
print(f'Todas as mulheres são: {mulheres}')
print(f'Todas as pessoas com idade acima da média são: {acima}')

