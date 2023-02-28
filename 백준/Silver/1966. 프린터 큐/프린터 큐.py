import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    d = deque()
    for i in range(N):
        d.append((A[i], i))

    cnt = 0
    while True:
        if max(d)[0] == d[0][0]:
            cnt += 1
            if d[0][1] == M:
                print(cnt)
                break
            else:
                d.popleft()
        else:
            d.append(d.popleft())