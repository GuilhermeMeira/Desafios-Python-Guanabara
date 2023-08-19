idade = cont18 = conth = contm20 = 0
sexo = continuar = ' '
while True:
    if continuar == 'N':
        break
    continuar = ' '
    sexo = ' '
    idade = int(input('Digite sua idade'))
    while sexo not in 'MF':
        sexo = input('Digite seu sexo M/F').upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm20 +=1
    while continuar not in 'SN':
        continuar = input('Deseja continuar? S/N').upper().strip()[0]
        if continuar == 'N':
            break




print(f'Existem {cont18} pessoas com mais de 18 anos.')
print(f'Existem {conth} homens cadastrados.')
print(f'Existem {contm20} mulheres com menos de 20 anos.')