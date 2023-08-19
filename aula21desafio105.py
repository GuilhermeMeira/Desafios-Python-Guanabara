def notas(*num, sit=True):
    '''
    Funçao para analisar notas de varios alunos
    :param num: notas
    :param sit: mostra a situaçao do aluno
    :return: um dicionario com a quantidade de notas, maior e menor nota e a média
    '''
    dici = {}
    dici['qnotas'] = len(num)
    dici['maiornota'] = max(num)
    dici['menornota'] = min(num)
    dici['media'] = (sum(num) / len(num))
    if sit == True:
        if dici['media'] >= 6:
            dici['situaçao'] = 'BOA'
        else:
            dici['situaçao'] = 'RUIM'
    return dici



resp = notas(2, 4, 5, 7, 10, sit=False)
print(resp)