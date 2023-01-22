N = int(input())
cnt = 1
while cnt <= N:
    print(('*' * cnt).rjust(N))
    cnt += 1