import sys
sys.setrecursionlimit(10**6)
    
def dfs(graph, v, visted):
    visted[v] = True
    for j in graph[v]:
        if not visted[j]:
            dfs(graph, j, visited)

N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for k in range(1, N+1):
    if not visited[k]:
        dfs(graph, k, visited)
        cnt += 1

print(cnt)