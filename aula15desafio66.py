n = s = cont = 0

while n != 999:
    n = int(input('Digite um número (999 para parar)'))
    if n == 999:
        break
    s += n
    cont +=1
print(f'Foram digitados  {cont} valores e a soma entre eles é {s}')