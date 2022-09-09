N = int(input())

for casos in range(N):
    x, y = input().split()
    x = int(x)
    y = int(y)
    acm = 0
    while (x > y):
        if (y % 2 == 0):
            y += 1
        elif (y % 2 != 0):
            y += 2
        if (x > y):
            acm += y
    while (x < y):
        if (x % 2 == 0):
            x += 1
        elif (x % 2 != 0):
            x += 2
        if (x < y):
            acm += x
    print(acm)
