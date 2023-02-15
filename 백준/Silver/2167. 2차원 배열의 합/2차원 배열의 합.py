import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(input())
for _ in range(K):
    result = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            result += arr[a][b]
    print(result)