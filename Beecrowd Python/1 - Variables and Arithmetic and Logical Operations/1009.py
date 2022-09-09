vendedor = input()
fixo = float(input())
vendas = float(input())
comissao = vendas / 100 * 15
total = fixo + comissao

print('TOTAL = R$ %0.2f' %total)
