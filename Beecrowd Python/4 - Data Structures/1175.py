n = []

for ctd in range(20):
    n.append(int(input()))

for ctd2 in range(10):
    temp = n[ctd2]
    n[ctd2] = n[len(n) -ctd2 - 1]
    n[len(n) -ctd2 - 1] = temp

for ctd3 in range(20):
    print('N[{0}] = {1}' .format(ctd3, n[ctd3]))
    
