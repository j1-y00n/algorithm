C = int(input())
pair = int(input())

graph = [[] for _ in range(C+1)]
result = []
for a in range(pair):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (C + 1)

def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

    return sum(visited)

print(dfs(graph, 1, visited)-1)