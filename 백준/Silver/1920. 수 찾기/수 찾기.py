import sys

N = int(input())
n = set(map(int, sys.stdin.readline().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().split()))
s_m = set(m)
a = n & s_m
for i in m:
    if i in a:
        print(1)
    else:
        print(0)