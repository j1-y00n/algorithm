from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs():
    queue = deque([N])
    
    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        else:
            for i in (x-1, x+1, x*2):
                if 0 <= i <= 100000 and visited[i] == 0:
                    visited[i] = visited[x] + 1
                    queue.append(i)
                    
print(bfs())