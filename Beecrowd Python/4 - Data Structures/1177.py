n = []
t = int(input())

for ctd in range(0, 1000, t):
    for ctd2 in range(t):
        n.append(ctd2)

for ctd3 in range(1000):
    print('N[{0}] = {1}' .format(ctd3, n[ctd3]))
