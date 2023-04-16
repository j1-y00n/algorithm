from collections import deque
import sys

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(a, b):
    visited[a][b] = True
    queue = deque()
    queue.append([a, b])

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > h and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = True

N = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = []

H = list(set([m for n in graph for m in n]))

for h in H:
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > h and visited[i][j] == False:
                bfs(i, j)
                cnt += 1
    result.append(cnt)

if len(H) == 1:
    print(1)
else:
    print(max(result))