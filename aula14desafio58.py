import random
c = 0
n1 = random.randint(0, 10)
n2 = int(input('Digite um número'))
while n2 != n1:
    n2 = int(input('Você errou, tente novamente:'))
    c += 1
print(f'Voce acertou com apenas {c + 1} tentativas')