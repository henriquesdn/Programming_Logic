n = []

n.append(float(input()))

for ctd in range(99):
    n.append(n[len(n) -1] / 2)

for ctd2 in range(100):
    print('N[{0}] = {1:.4f}' .format(ctd2, n[ctd2]))
