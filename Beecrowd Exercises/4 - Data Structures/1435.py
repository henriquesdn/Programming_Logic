tela = []

n = int(input())

acm = 0

while n != 0:
    for ctd in range(n):
        tela.append([1] * n)

    acm += 1

    n = int(input())

for ctd2 in range(0 ,len(tela), len(tela[ctd2])):
    for ctd3 in range(tela[ctd2]):
        print(tela[ctd2 + ctd3])
