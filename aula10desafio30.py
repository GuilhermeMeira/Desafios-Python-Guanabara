
cores = {'azul' : '\033[34m',
         'roxo' : '\033[35'


}
n = int(input('Digite um número: '))

if n % 2 == 0:
    print('Esse número é  par')
else:
    print('Esse número é impar')

print(cores['azul'],'banana')