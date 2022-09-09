tela = []
for ctd in range(12):
    tela.append([0] * 12)

o = input() #S ou M
acm = 0
acm2 = 0

for ctd2 in range(12):
    for ctd3 in range(12):
        tela[ctd2][ctd3] = float(input())

for ctd4 in range(12):
    for ctd5 in range(12):
        if ctd4 < ctd5:
            acm += tela[ctd4][ctd5]
            acm2 += 1

if o == 'S':
    print('{0:.1f}' .format(acm))
elif o == 'M':
    print('{0:.1f}' .format(acm / acm2))
