gi, gg = input().split()

gi = int(gi)
gg = int(gg)
vi = 0
vg = 0
emp = 0
gren = 0

if (gi > gg):
    vi += 1
elif (gi < gg):
    vg += 1
else:
    emp += 1

gren += 1

print('Novo grenal (1-sim 2-nao)')
new = int(input())

while (new == 1):
    gi, gg = input().split()
    
    gi = int(gi)
    gg = int(gg)

    if (gi > gg):
        vi += 1
    elif (gi < gg):
        vg += 1
    else:
        emp += 1

    gren += 1

    print('Novo grenal (1-sim 2-nao)')
    new = int(input())

if (vi == vg):
    print('{0} grenais\nInter:{1}\nGremio:{2}\nEmpates:{3}\nNao houve vencedor' .format(gren, vi, vg, emp))
elif (vi > vg):
    print('{0} grenais\nInter:{1}\nGremio:{2}\nEmpates:{3}\nInter venceu mais' .format(gren, vi, vg, emp))
elif (vi < vg):
    print('{0} grenais\nInter:{1}\nGremio:{2}\nEmpates:{3}\nGremio venceu mais' .format(gren, vi, vg, emp))
