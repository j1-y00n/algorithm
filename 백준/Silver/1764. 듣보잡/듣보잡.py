import sys

N, M = list(map(int, sys.stdin.readline().split()))
n = {sys.stdin.readline().strip() for _ in range(N)}
m = {sys.stdin.readline().strip() for _ in range(M)}
result = sorted(list(n & m))
print(len(result))
for i in result:
    print(i)