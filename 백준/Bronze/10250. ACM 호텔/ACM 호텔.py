T = int(input())
for _ in range(T):
    H, W, N = list(map(int, input().split()))
    a = N//H
    b = N%H
    if b == 0:
        print(H*100 + a)
    else: 
        print(b*100 + a + 1)