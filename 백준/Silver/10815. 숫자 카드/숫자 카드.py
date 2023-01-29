import sys

li = []
N = int(input())
n = set(map(int, sys.stdin.readline().split()))
M = int(input())
m = list(map(int, sys.stdin.readline().split()))
li = [] 
for i in m:
    if i in n:
        li.append(1)
    else:
        li.append(0)
print(*li)