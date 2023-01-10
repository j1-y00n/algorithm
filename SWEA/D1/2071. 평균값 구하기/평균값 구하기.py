T = int(input())
for t in range(1, T+1):
    a = list(map(int, input().split()))
    s = sum(a)
    result = round(s/10)
    print(f'#{t} {result}')