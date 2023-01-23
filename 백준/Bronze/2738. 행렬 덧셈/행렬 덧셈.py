N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for i1 in range(N)]
B = [list(map(int, input().split())) for i2 in range(N)]
for i3, i4 in zip(A, B):
    C = [i5 + i6 for i5, i6 in zip(i3, i4)]
    print(*C)