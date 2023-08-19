
par1 = 0
par2 = 0
lista2 =[]
lista = str(input("Digite a expressão"))


# for palavra in lista:
#     for caracter in palavra:
#         if caracter == "(":
#             par1 += 1
#         elif caracter == ")":
#             par2 += 1
#
# if par1 == par2:
#     print("A expressão está correta!")
# else:
#     print("A expressão está errada ! ")

for simb in lista:
    if simb == '(':
        lista2.append('(')
    elif simb == ')':
        if len(lista2) > 0:
            lista2.pop()

if len(lista2) > 0:
    print("expressao incorreta")
else:
    print("expressao correta")