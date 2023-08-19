import random
aluno1 = input('Nome do aluno1: ')
aluno2 = input('Nome do aluno2: ')
aluno3 = input('Nome do aluno3: ')
aluno4 = input('Nome do aluno4: ')

lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f'A ordem de apresentaçao dos alunos {aluno1}, {aluno2}, {aluno3}, {aluno4} \nSerá a seguinte: {list}')
