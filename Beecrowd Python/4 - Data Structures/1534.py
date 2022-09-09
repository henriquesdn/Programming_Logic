while True:
    try:
        n = int(input())

        tela = []

        for ctd in range(n):
                 tela.append([3] * n)

        for ctd2 in range(n):
            for ctd3 in range(n):
                if ctd2 == ctd3:
                    tela[ctd2][ctd3] = 1

        for ctd4 in range(n):
            for ctd5 in range(n):
                if len(tela) - ctd4 - 1 == ctd5:
                    tela[ctd4][ctd5] = 2
                

        for ctd6 in range(n):
            print(*tela[ctd6], sep = '')            
    except EOFError:
        break

