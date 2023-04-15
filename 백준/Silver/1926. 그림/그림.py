import sys
sys.setrecursionlimit(10**6)

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    global cnt
    graph[x][y] = 0

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny)

n, m = map(int, input().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0
area = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 1
            dfs(i, j)
            result += 1
            area.append(cnt)

if result == 0:
    print(result, 0, sep = '\n')
else:
    print(result, max(area), sep = '\n')