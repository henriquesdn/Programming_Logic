x1, y1 = input().split()
x2, y2 = input().split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
paren1 = x2 - x1
paren2 = y2 - y1
equacao = paren1 ** 2 + paren2 ** 2
raizq = equacao ** 0.5

print('%0.4f' %raizq)
