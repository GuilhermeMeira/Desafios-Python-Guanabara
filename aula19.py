# pessoa1 = {'nome': 'Gustavo',
#            'sexo': 'M',
#            'idade': 22}
# pessoa2 = {'nome': 'William',
#            'sexo': 'F',
#            'idade': 24}
# galera = []
#
# galera.append(pessoa1)
# galera.append(pessoa2)
#
# for x in range(0,2):
#     print(galera[x]['nome'], galera[x]['idade'])
#
estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = input("UNIDADE FEDERATIVA: ")
    estado['sigla'] = input("SIGLA: ")
    brasil.append(estado.copy())

for estado in brasil:
    for key, v in estado.items():
        print(f'o campo {key} tem valor {v}' , end=' ')
    print()