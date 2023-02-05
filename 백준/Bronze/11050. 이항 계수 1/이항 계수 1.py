N, K = list(map(int, input().split()))

n = 1
for i in range(1, N + 1):
    n *= i

k = 1
for j in range(1, K + 1):
    k *= j
    
a = 1
for b in range(1, N - K + 1):
    a *= b

print(int(n/(k*a)))