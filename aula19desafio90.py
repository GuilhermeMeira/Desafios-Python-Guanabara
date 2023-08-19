aluno = {}

aluno['Nome'] = input('Digite um nome: ')
aluno['Média'] = int(input(f'Digite a média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situaçao'] = 'Aprovado'
else:
    aluno['Situaçao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')