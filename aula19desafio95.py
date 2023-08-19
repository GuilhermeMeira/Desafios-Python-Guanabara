jogadores = []
jogador = {}
gols = []
while True:
    jogador['nome'] = input("Nome:")
    jogador['partidas'] = int(input("Partidas:"))
    for x in range(0, jogador['partidas']):
        gol = int(input(f"Quantos gols na partida {x}"))
        gols.append(gol)
        jogador['gols'] = gols[:]
    jogadores.append(jogador.copy())
    gols.clear()
    continuar = input("Deseja continuar? S/N")
    if continuar.upper() == 'N':
        break
print(jogadores)
print(f'Cod Nome     gols     total')
print("-" * 35)
for x in range(0, len(jogadores)):
    print(f'{x} {jogadores[x]["nome"]}     {jogadores[x]["gols"]}     {sum(jogadores[x]["gols"])}')
while True:
    cod = int(input("Qual jogador deseja ver? 999 para parar"))
    if cod == 999:
        break
    if cod > len(jogadores) or cod < 0:
        print('Código inválido, tente novamente:')
    print(f'Levantamento do jogador: {jogadores[cod]["nome"]}')
    for z in range(0, jogadores[cod]["partidas"]):
        print(f"Na partida {z} o jogador fez {jogadores[cod]['gols'][z]} gols")


