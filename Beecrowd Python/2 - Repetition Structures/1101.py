m, n = input().split()

m = int(m)
n = int(n)

while (m > 0) and (n > 0):
    acm = 0
    
    if (m > n):
        maior = m
        menor = n
    elif (m < n):
        maior = n
        menor = m

    for x in range(menor, maior + 1, 1):
        print(x, end = ' ')

        acm += x
        
    print('Sum={0}' .format(acm))

    m, n = input().split()

    m = int(m)
    n = int(n)
