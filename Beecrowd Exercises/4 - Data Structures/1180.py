n = int(input())

x = list(map(int,input().split()))

for ctd in range(n):
    if (x[ctd] == min(x)):
        print('Menor valor: {0}\nPosicao: {1}' .format(x[ctd], ctd))
        
