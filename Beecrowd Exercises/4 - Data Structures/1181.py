tela = []
for ctd in range(12):
    tela.append([0] * 12)

L = int(input())
t = input() #S ou M
acm = 0

for ctd2 in range(12):
    for ctd3 in range(12):
        tela[ctd2][ctd3] = float(input())

for ctd4 in range(12):
        acm += tela[L][ctd4]

if t == 'S':
    print('{0:.1f}' .format(acm))
elif t == 'M':
    print('{0:.1f}' .format(acm / 12))
