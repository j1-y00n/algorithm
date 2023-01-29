import sys

d = {}
N = int(input())
n = list(map(int, sys.stdin.readline().split()))
for i in n:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

M = int(input())
m = list(map(int, sys.stdin.readline().split()))
for i in m:
    if i in d:
        print(d[i], end = " ")
    else:
        print(0, end = " ")