import sys

n = int(input())
graph = [[] for _ in range(n+1)]
a, b = map(int, sys.stdin.readline().split())
m = int(input())
for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)
result = []

def dfs(start, cnt):
    cnt += 1
    visited[start] = True
    if start == b:
        result.append(cnt)   
    for j in graph[start]:
        if not visited[j]:
            dfs(j, cnt)
    
dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)