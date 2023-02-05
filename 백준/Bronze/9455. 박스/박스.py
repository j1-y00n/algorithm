import sys

for _ in range(int(input())):
    m, n = list(map(int, input().split()))
    grid = [input().split() for _ in range(m)]

    grid2 = [[grid[i][j] for i in range(m)] for j in range(n)]

    cnt = 0

    for a in grid2:
        for b in range(m-1):
            if a[b] == '1':
                cnt += a[b+1:].count('0')
    print(cnt)