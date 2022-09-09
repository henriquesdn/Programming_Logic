n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

med = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

if (med >= 7):
    print('Media: {0:.1f}\nAluno aprovado.' .format(med))
elif (med >= 5):
    exam = float(input())
    fim = (med + exam) /2
    if (fim >= 5):
        print('Media: {0:.1f}\nAluno em exame.\nNota do exame: {1:.1f}\nAluno aprovado.\nMedia final: {2:.1f}' .format(med, exam, fim))
    else:
        print('Media: {0:.1f}\nAluno em exame.\nNota do exame: {1:.1f}\nAluno reprovado.\nMedia final: {2:.1f}' .format(med, exam, fim))
elif (med < 5):
    print('Media: {0:.1f}\nAluno reprovado.' .format(med))
