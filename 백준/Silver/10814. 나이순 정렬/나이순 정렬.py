import sys

m = []
N = int(input())
for _ in range(N):
    age, name = sys.stdin.readline().split()
    m.append((age, name))
m.sort(key = lambda x : int(x[0]))
for a, n in m:
    print(a, n)