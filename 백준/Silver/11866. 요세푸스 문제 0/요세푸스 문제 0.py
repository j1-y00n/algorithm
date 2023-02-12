from collections import deque

N, K = list(map(int, input().split()))
li = deque(i for i in range(1, N+1))
result = list()
while li:
    li.rotate(- K + 1)
    a = li.popleft()
    result.append(a)


print("<", end="")
print(*result, sep=", ", end="")
print(">")