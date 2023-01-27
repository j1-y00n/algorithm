import sys

N = int(input())
words = {sys.stdin.readline().strip() for _ in range(N)}
li = []
for w in words:
    li.append((len(w), w))
s = sorted(li)
for k, v in s:
    print(v)