import sys

T = int(input())
for _ in range(T):
    A, B = list(map(int,(sys.stdin.readline().split())))
    print(A + B)