from collections import deque
import sys

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(a, b):
    global cnt
    cnt = 1
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append([nx, ny])                

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
cnt = 0
house = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            house.append(cnt)

house.sort()
print (len(house), *house, sep='\n')