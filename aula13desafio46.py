from time import sleep

print('Contagem regressiva:')

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[1;31mB\033[33mO\033[33mO\033[31mM') #boom pintado