import time
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'arquivo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome:')
        idade = leiaint('Idade')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('ERRO, DIGITE UM OPÇÃO VÁLIDA')
    time.sleep(1.5)
