import sys

d = {}
d_li = []
N, M = list(map(int, sys.stdin.readline().split()))
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    d[name] = i
    d_li.append(name)
    
for j in range(M):
    m = sys.stdin.readline().strip()
    if m.isalpha():
        print(d[m])  
    else:
        print(d_li[int(m)-1])