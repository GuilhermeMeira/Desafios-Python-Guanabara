from time import sleep


def maior(*num):
    maior = 0
    for n in num:
        sleep(0.3)
        print(n, end=' ')
        if n >= maior:
            maior = n
    print(f' Foram passados {len(num)} valores ao todo e o maior é: {maior}')


maior(3, 5, 6, 32, 234, 4, 5, 6, 1000)

maior(2, 3, 3, 4, 5, 6, 7, 313, 2222222222, 444444444444)