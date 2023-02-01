import sys

for _ in range(int(input())):
    score = list(map(int, sys.stdin.readline().split()))
    score2 = sorted(score)
    if score2[3] - score2[1] >= 4:
        print('KIN')
    else:
        print(sum(score2[1:4]))
