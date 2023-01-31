import sys

num = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

li = []
max_num = -1
for i in range(9):
    for j in range(9):
        if num[i][j] > max_num:
            max_num = num[i][j]
            li.append((i + 1, j + 1))
print(max_num)      
print(*li.pop())