# help()
#
# def somar(a=0, b=0, c=0):
#     s = a+b+c
#     return s
#
#
# print(somar(3, 5, 7))


def fatorial(num=1):
    n = 1
    for x in range(num, 0, -1):
        n = n*x
    return n


print(fatorial(6))