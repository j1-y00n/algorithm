import sys

white = [[0]*101 for _ in range(101)]

for _ in range(int(input())):
    x, y = list(map(int, sys.stdin.readline().split()))
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            white[i][j] = 1

print(sum(sum(white, [])))