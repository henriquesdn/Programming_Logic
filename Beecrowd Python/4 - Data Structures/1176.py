fib = [0, 1]

t = int(input())

for ctd in range(t):
    n = int(input())
    
    while (len(fib) -1 < n):
        fib.append(fib[len(fib) -1] + fib[len(fib) -2])

    print('Fib({0}) = {1}' .format(n, fib[n]))

    fib = [0, 1]

