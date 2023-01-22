C = int(input())
for i in range(C):
    N = list(map(int, input().split()))
    average = (sum(N)-N[0])/N[0]
    cnt = 0
    for j in N[1:]:
        if j > average:
            cnt += 1
    print(f'{(cnt/N[0])*100:.3f}%')
