# galera = [["Gui", 19], ["Binga", 23], ["Aa", 50]]
#
# for x in galera:
#     print(x[0])


pessoas = list()
dado = list()

for u in range(0,3):
    dado.append(input("Nome:"))
    dado.append(int(input("Idade:")))
    pessoas.append(dado[:])
    dado.clear()

for p in pessoas:
    if p[1] > 18:
        print(f"{p[0]} é maior de idade")