from datetime import datetime
ano = datetime.now().year
trabalho = {'nome': input("Nome:"), 'anonasc': int(input("Data de nascimento"))}
trabalho['idade'] = ano - trabalho['anonasc']
trabalho['ctps'] = int(input('Carteira de Trabalho (0 não tem)'))
if trabalho['ctps'] != 0:
    trabalho['contratação'] = int(input('Qual seu ano de contratação?'))
    trabalho['salario'] = int(input('Qual o seu salário?'))
    trabalho['aposentadoria'] = (trabalho['contratação'] + 35) - trabalho['anonasc']
for k, v in trabalho.items():
    print(f' {k} tem valor {v}')
