a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)
maiorab = (a + b + abs(a - b)) / 2
maior = int((maiorab + c + abs(maiorab - c)) / 2)

print(maior, 'eh o maior')
    
