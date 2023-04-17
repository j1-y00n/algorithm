from collections import deque
import sys

M, N = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
queue = deque()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()
day = 0
for tomatos in graph:
    for t in tomatos:
        if t == 0:
            print(-1)
            exit()
    day = max(day, max(tomatos))
print(day - 1)