N = int(input())
result = 0
while N > 0:
    a= N % 10
    result += a
    N = N // 10
print(result)


