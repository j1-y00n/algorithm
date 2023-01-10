T = int(input())
for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    몫 = a//b
    나머지 = a%b
    print(f'#{t} {몫} {나머지}')