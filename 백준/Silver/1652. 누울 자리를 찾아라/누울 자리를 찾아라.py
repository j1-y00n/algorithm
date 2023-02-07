import sys

N = int(input())
room = [list(input()) for _ in range(N)]

result1 = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        elif room[i][j] == 'X':
            if cnt >= 2:
                result1 += 1
                cnt = 0
            else:
                cnt = 0
        if j == N-1:
            if cnt >= 2:
                result1 += 1

result2 = 0
for j in range(N):
    cnt = 0
    for i in range(N):
        if room[i][j] == '.':
            cnt += 1
        elif room[i][j] == 'X':
            if cnt >= 2:
                result2 += 1
                cnt = 0
            else:
                cnt = 0
        if i == N-1:
            if cnt >= 2:
                result2 += 1

print(result1, result2)