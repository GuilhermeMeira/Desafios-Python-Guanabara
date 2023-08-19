var = input('Digite qualquer coisa !')

print(var, 'é do tipo: ',(type(var)))

print('é um alfanumerico?',var.isalnum()) #metodo do curso

#meu metodo
if var.isalnum():
    print(var, ' É um alfanumerico')
else :
    print(var, ' Não é alfanumérico')

if var.isalpha():
    print(var, ' é alfabetico')
else :
    print(var, ' Não é alfabetico')

if var.isnumeric():
    print(var, ' é numérico')
else :
    print(var, ' Não é numérico')
