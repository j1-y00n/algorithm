N = input()
for i in N:
    print(N[:10])
    N = N.replace(N[:10], '')
    if len(N) == 0:
        break