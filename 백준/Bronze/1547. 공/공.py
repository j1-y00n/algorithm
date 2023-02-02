import sys

cup = [1, 2, 3]
cnt = int(input())
for _ in range(cnt):
    x, y = map(int, sys.stdin.readline().split())
    for index, value in enumerate(cup):
        if value == x:
            cup[index] = y
        if value == y:
            cup[index] = x
print(cup[0])