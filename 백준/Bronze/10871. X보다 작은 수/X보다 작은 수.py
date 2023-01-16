N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
list = []
for i in A:
    if i < X:
        list.append(i)
print(*list)