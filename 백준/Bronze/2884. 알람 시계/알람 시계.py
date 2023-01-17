H, M = list(map(int, input().split()))

time = (H * 60) + M - 45
if time // 60 < 0:
    print(24+(time // 60), time % 60)
    
else:
    print(time // 60, time % 60)
