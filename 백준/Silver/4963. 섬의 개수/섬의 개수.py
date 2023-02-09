import sys
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0

        dfs(x - 1, y)
        dfs(x +1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y -1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        return True
    return False

while True:
    w, h = map(int, input().split())   # w:열 h:행

    if w == h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    result = 0
    for a in range(h):
        for b in range(w):
            if dfs(a, b) == True:
                result += 1

    print(result)