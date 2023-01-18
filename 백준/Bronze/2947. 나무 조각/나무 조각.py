T = list(map(int, input().split()))
li = [1, 2, 3, 4, 5]
while T != li:
    for i in range(4):
        if T[i] > T[i+1]:
            T[i], T[i+1] = T[i+1], T[i]
            print(*T)