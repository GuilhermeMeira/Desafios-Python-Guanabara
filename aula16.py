lanche = ('Hambúrguer', 'Suco','Pizza','Pudim')

for comida in lanche:
    print(comida)

for cont in range(0,len(lanche)):
    print(lanche[cont], cont)

for num, comida in enumerate(lanche):
    print(comida, num)

print(sorted(lanche)) #ordem alfabética

c = (5, 3, 2, 1)
print(sorted(c))# menor para o maior