num = int(input())
acm = 0

for x in range(num):
    acm += 1
    qua = acm * acm
    cub = qua * acm
    print(acm, qua, cub)
