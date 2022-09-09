x, y = input().split()

x = int(x)
y = int(y)
acm = 0
acm2 = 0

for a in range(1, y + 1, x):
        for b in range(x):
            acm += 1
            acm2 += 1
            if (acm2 < x):
             print(acm, end = ' ')
            else:
                print(acm)
        acm2 = 0
