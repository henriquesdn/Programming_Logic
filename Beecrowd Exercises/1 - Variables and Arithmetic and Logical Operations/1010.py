codp1, nump1, valop1 = input().split()
codp2, nump2, valop2 = input().split()

codp1 = int(codp1)
nump1 = int(nump1)
valop1 = float(valop1)
codp2 = int(codp2)
nump2 = int(nump2)
valop2 = float(valop2)

peca1 = nump1 * valop1
peca2 = nump2 * valop2
total = peca1 + peca2

print('VALOR A PAGAR: R$ %0.2f' %total)
