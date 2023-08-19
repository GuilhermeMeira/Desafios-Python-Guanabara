n = int(input('Digite um número inteiro'))

t0 = 0
t1 = 1
c = 3
print(t0)
print(t1)
while c <= n:
    tn = t0 + t1
    print(tn)
    t0 = t1
    t1 = tn
    c += 1

