import sys
from collections import deque

for _ in range(int(input())):
    score = list(map(int, sys.stdin.readline().split()))
    score2 = deque(sorted(score))
    score2.pop()
    score2.popleft()
    if score2[2] - score2[0] >= 4:
        print('KIN')
    else:
        print(sum(score2))