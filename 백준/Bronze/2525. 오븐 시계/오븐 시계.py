H, M = list(map(int, input().split()))
M2 =int(input())
time = (H * 60) + M + M2
print((time // 60) %24, time % 60)