import sys

input()
n = set(sys.stdin.readline().split())
input()
m = sys.stdin.readline().split()
for i in m:
    if i in n:
        print(1)
    else:
        print(0)