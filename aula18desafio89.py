listona = []
aluno = []
nome = []
nota = []
cod = 0
while True:
    nome.append(input("Nome:"))
    for i in range(0, 2):
        nota.append(int(input("Nota:")))
    aluno.append(nome[:])
    aluno.append(nota[:])
    listona.append(aluno[:])
    aluno.clear()
    nome.clear()
    nota.clear()
    continuar = input("Deseja continuar? S/N")
    if continuar.upper() == "N":
        print("Fim do programa ! ")
        break
for j in range(0, len(listona)):
    print(f'O aluno({j}):{listona[j][0]} teve média {sum(listona[j][1]) / 2}')
while True:
    cod = int(input("Mostra nota de qual aluno? (999 para parar)"))
    if cod == 999:
        break
    print(f'O aluno {listona[cod][0]} tirou: {listona[cod][1]}')

print(listona)
