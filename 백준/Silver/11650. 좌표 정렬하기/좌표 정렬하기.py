import sys

xy = []
N = int(input())
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    xy.append((a[0], a[1]))
xy.sort()
for x, y in xy:
    print(x, y)