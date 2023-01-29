import sys

N = int(input())
n = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    n[num] += 1

for j in range(10001):
    if n[j] != 0:
        for _ in range(n[j]):
            print(j)