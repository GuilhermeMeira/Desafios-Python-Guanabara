from aula22 import ex109 

n = int(input('Digite um número:'))

print(f'Aumentando 10% de {ex109.moeda(n)} temos {ex109.aumentar(n,10, form=True)}')
print(f'Diminuindo 15% de {ex109.moeda(n)} temos {ex109.diminuir(n,15, form=True)}')
print(f'Dobrando {ex109.moeda(n)} temos {ex109.dobro(n, form=True)}')
print(f'A metade de {ex109.moeda(n)} é {ex109.metade(n, form=True)}')