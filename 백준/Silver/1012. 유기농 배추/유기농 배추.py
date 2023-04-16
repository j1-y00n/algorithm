from collections import deque
import sys

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = 0

T = int(input())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0]*M for _ in range(N)]

    for k in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
                
    print(cnt)