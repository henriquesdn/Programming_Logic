    par = []
    impar = []

    for ctd in range(15):
        x = int(input())

        if (x % 2 == 0):
            par.append(x)
        else:
            impar.append(x)

        if (len(par) == 5):
            for ctd2 in range(5):
                print('par[{0}] =' .format(ctd2), par[ctd2])

            par = []
        elif (len(impar) == 5):
            for ctd3 in range(5):
                print('impar[{0}] =' .format(ctd3), impar[ctd3])

            impar = []

    for ctd4 in range(len(impar)):
        print('impar[{0}] =' .format(ctd4), impar[ctd4])

    for ctd5 in range(len(par)):
        print('par[{0}] =' .format(ctd5), par[ctd5])

