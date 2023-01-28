import sys
import heapq

h = []
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(h, -x)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)