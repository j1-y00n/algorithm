import sys

num = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_num = max(sum(num, []))
print(max(sum(num, [])))

for i in range(9):
    for j in range(9):
        if num[i][j] == max_num:
            print(i + 1, j + 1)