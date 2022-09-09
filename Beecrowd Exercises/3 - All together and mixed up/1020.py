dias = int(input())

ano = dias // 365
mes = dias % 365 // 30
dia = dias % 365 % 30

print('%i ano(s)' %ano)
print('%i mes(es)' %mes)
print('%i dia(s)' %dia)
