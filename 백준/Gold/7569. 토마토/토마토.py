from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
direction = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0)]
queue = deque()

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in direction:
            nz = z + dz
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and graph[nz][nx][ny] == 0:
                queue.append([nz, nx, ny])
                graph[nz][nx][ny] = graph[z][x][y] + 1

for h in range(H):
    for i in range(N):
        for j in range(M):
            if graph[h][i][j] == 1:
                queue.append([h, i, j])

bfs()
day = 0
for tomatos in graph:
    for tomato in tomatos:
        for t in tomato:
            if t == 0:
                print(-1)
                exit()
        day = max(day, max(tomato))
print(day - 1)