I = 0
J = 1
dec = 2

while (I <= 2):
    print('I=%i' %I, 'J=%i' %J)
    print('I=%i' %I, 'J=%i' %(J + 1))
    print('I=%i' %I, 'J=%i' %(J + 2))
    while (I < 2 and dec < 9):
        print('I=%i' %I + '.%i' %dec, 'J=%i' %J + '.%i' %dec)
        print('I=%i' %I + '.%i' %dec, 'J=%i' %(J + 1) + '.%i' %dec)
        print('I=%i' %I + '.%i' %dec, 'J=%i' %(J + 2) + '.%i' %dec)
        dec += 2
    dec = 2
    I += 1
    J += 1
