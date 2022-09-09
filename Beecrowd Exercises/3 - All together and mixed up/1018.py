valor = int(input())

c100 = valor // 100
c50 = valor % 100 // 50
c20 = valor % 100 % 50 // 20
c10 = valor % 100 % 50 % 20 // 10
c5 = valor % 100 % 50 % 20 % 10 // 5
c2 = valor % 100 % 50 % 20 % 10 % 5 // 2
c1 = valor % 100 % 50 % 20 % 10 % 5 % 2 // 1

print(valor)
print('%i nota(s) de R$ 100,00' %c100)
print('%i nota(s) de R$ 50,00' %c50)
print('%i nota(s) de R$ 20,00' %c20)
print('%i nota(s) de R$ 10,00' %c10)
print('%i nota(s) de R$ 5,00' %c5)
print('%i nota(s) de R$ 2,00' %c2)
print('%i nota(s) de R$ 1,00' %c1)
