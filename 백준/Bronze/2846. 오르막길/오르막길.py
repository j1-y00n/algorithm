import sys

N = int(input())
P = list(map(int, sys.stdin.readline().split()))
start = P[0]
h = 0
height = []

for i in P:
    if i > start:
        cnt = i - start
        h += cnt

    else:
        height.append(h)
        h = 0

    start = i

height.append(h)
print(max(height))