import random
a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
e = random.randint(0,10)
tupla =  (a, b, c, d, e)
maior = max(tupla)
menor = min(tupla)
#2 formas de cima é mais prática a de baixo é mais lógica
maior2 = sorted(tupla)[4]
menor2 = sorted(tupla)[0]
print(f'Os números gerados foram{tupla}')
print(f'O maior número foi {maior2} e o menor foi {menor2}')