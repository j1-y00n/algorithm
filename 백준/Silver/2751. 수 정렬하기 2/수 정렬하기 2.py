import sys
import heapq

h = []
N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    heapq.heappush(h, num)
while h:
    print(heapq.heappop(h))