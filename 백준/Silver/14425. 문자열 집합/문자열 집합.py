N, M = list(map(int, input().split()))
S = {input() for _ in range(N)}
cnt = 0
for _ in range(M):
    test = input()
    if test in S:
        cnt += 1
print(cnt)