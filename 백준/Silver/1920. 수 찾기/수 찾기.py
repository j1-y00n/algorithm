import sys

input()
n = set(sys.stdin.readline().split())
input()
m = sys.stdin.readline().split()
a = n & set(m)
for i in m:
    if i in a:
        print(1)
    else:
        print(0)