import sys

li = []
N = int(input())
for _ in range(N):
    x, y = list(map(int, sys.stdin.readline().split()))
    li.append((x, y))

s_li = sorted(li, key=lambda x: (x[1], x[0]))
for a, b in s_li:
    print(a, b)