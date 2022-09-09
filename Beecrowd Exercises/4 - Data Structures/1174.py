a = []

for ctd in range(100):
    a.append(eval(input()))

    if (a[len(a) -1] <= 10):
        print('A[{0}] = {1:.1f}' .format(len(a) -1, a[len(a) -1]))
