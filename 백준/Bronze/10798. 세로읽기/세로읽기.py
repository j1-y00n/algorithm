import sys


a = [['@']*15 for _ in range(5)]

for i in range(5):
    word = list(sys.stdin.readline().strip())
    for j in range(len(word)):
        a[i][j] = word[j]

for y in range(15):
    for x in range(5):
        if a[x][y] != '@':
            print(a[x][y], end= '')