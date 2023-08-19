def ficha(nome='Não informado', gols=0):
    nome = input('Nome do jogador:')
    if nome == '':
        nome = "<Não informado>"
    gols = input("Gols:")
    if gols == '' or not gols.isnumeric():
        gols = 0
    print("=-" * 20)
    print(f'O jogador {nome} marcou {gols} gols')
    print("=-" * 20)


ficha()
