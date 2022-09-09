cod, qtd = input().split()

cod = int(cod)
qtd = int(qtd)

if (cod == 1):
    print('Total: R$ {0:.2f}' .format(4 * qtd))
elif (cod == 2):
    print('Total: R$ {0:.2f}' .format(4.5 * qtd))
elif (cod == 3):
    print('Total: R$ {0:.2f}' .format(5 * qtd))
elif (cod == 4):
    print('Total: R$ {0:.2f}' .format(2 * qtd))
elif (cod == 5):
    print('Total: R$ {0:.2f}' .format(1.5 * qtd))
