N = int(input())

M = 0
while N > M:
    result = 0
    for i in str(M):
        result += int(i)   
    if M + result == N:
        print(M)
        break
    M += 1
if M == N:
    print(0)