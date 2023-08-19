from aula22 import ex108


n = int(input('Digite um número:'))

print(f'Aumentando 10% de {ex108.moeda(n)} temos {ex108.moeda(ex108.aumentar(n,10))}')
print(f'Diminuindo 15% de {ex108.moeda(n)} temos {ex108.moeda(ex108.diminuir(n,15))}')
print(f'Dobrando {ex108.moeda(n)} temos {ex108.moeda(ex108.dobro(n))}')
print(f'A metade de {ex108.moeda(n)} é {ex108.moeda(ex108.metade(n))}')