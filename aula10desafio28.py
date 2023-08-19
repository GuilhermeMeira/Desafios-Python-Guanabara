import random
import time
n1 = random.randint(0, 5)

n2 = int(input("Pensei em um número de 0 a 5, tente acertar que número é esse: "))

print('\033[1;36m PROCESSANDO...')
time.sleep(2)

if n1 == n2:
    print("\033[1;32mParabéns, você acertou !")
else:
    print(f'\033[1;31m Você perdeu, eu pensei no número {n1}')
