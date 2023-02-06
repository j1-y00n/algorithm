C = int(input())
pair = int(input())

graph = [[] for _ in range(C+1)]
result = []
for a in range(pair):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [False] * (C + 1)

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    
    return sum(visited)

print(dfs(1)-1)