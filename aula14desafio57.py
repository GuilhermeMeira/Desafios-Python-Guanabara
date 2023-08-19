sexo = input('Digite o seu sexo:').upper().strip()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo [M/F]')).upper().strip()
print(f'Parabéns, você digitou {sexo} corretamente!')
