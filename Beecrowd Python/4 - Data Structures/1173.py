n = []

n.append(int(input()))

print('N[{0}] =' .format(len(n) -1), n[len(n) -1])

for ctd in range(9):
    n.append(2 * n[len(n) -1])

    print('N[{0}] =' .format(len(n) -1), n[len(n) -1])
    
