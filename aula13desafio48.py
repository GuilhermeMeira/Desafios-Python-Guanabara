s = 0
c = 0
for x in range(1, 501):
    if x % 2 != 0:
        if x % 3 == 0:
            s += x
            c += 1
print(f'A soma dos {c} valores é {s}')


