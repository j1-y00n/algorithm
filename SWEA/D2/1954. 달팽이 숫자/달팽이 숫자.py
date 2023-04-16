T = int(input())
for t in range(1, T+1):
    N = int(input())
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    snail = [[0]*N for _ in range(N)]
    num = 1
    D = 0
    x, y = 0, -1

    while num <= (N*N):
        nx = x + direction[D][0]
        ny = y + direction[D][1]
            
        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            snail[nx][ny] = num
            num += 1
            x, y = nx, ny
        else:
            D = (D+1) % 4
        
    print(f"#{t}")
    for s in snail:
        print(*s)