x = []

for ctd in range(10):
    x.append(int(input()))

    if (x[ctd] <= 0):
        x[ctd] = 1

    print('X[{0}] =' .format(ctd), x[ctd])
