a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if ((b ** 2 - 4 * a * c) ** 0.5 < 0) or (a == 0):
    print('Impossivel calcular')
else:
    br1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    br2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print('R1 = %.5f' %br1)
    print('R2 = %.5f' %br2)
