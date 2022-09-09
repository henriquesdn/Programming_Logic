segundos = int(input())
hora = segundos // 3600
minuto = segundos % 3600 // 60
segundo = segundos % 3600 % 60

print(str(hora) + ':' + str(minuto) + ':' + str(segundo))
