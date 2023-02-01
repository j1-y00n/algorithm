import sys

N, M = map(int, input().split())
n = list(map(int, sys.stdin.readline().split()))

max_num = 0
for i in range(N - 2):
    for j in range(i + 1, N -1):
        for k in range(j + 1, N):
            total = n[i] + n[j] + n[k]

            if max_num < total <= M:
                max_num = total
            
print(max_num)