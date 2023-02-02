import sys

xy = []
N = int(input())
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    xy.append([x, y])

rank = []

for i in range(N):
    cnt = 0
    for j, k in xy:
        if xy[i][0] < j and xy[i][1] < k:
            cnt += 1
    rank.append(cnt + 1)    
print(*rank)