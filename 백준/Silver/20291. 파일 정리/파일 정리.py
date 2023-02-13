import sys

N = int(input())
file = {}
for _ in range(N):
    name = (sys.stdin.readline().strip().split('.'))[1]
    if name not in file:
        file[name] = 1
    else:
        file[name] += 1

sort_file = sorted(file.items(), key = lambda X: X[0])
for k, v in sort_file:
    print(k, v)