lista = []
par = []
impar = []
while True:
    lista.append(int(input("Digite um número ! ")))
    continuar = input("Deseja continuar? S/N")
    if continuar.upper() == 'N':
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(lista)
print(par)
print(impar)