#listapeso = []
#for c in range(0,5):
  #  peso = float(input('Digite o seu peso'))
   # listapeso.append(peso)
#print(f' O maior peso é {max(listapeso)}kg')
#print(f' O menor peso é {min(listapeso)}kg ')



maxpeso = 0
minpeso = 0
for c in range(1,6):
    peso = float(input(f'Digite o peso da pessoa {c}'))
    if c == 1:
        maxpeso = peso
        minpeso = peso
    elif peso > maxpeso:
        maxpeso = peso
    elif peso < minpeso:
        minpeso = peso

print(f'O menor peso lido foi {minpeso}')
print(f'O maior peso lido foi {maxpeso}')
