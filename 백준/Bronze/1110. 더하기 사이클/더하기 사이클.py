N = input()
int_N = int(N)
cnt = 0

while True:
    a = int_N % 10
    b = (int_N // 10) + (int_N % 10)
    result = (a * 10) + (b % 10)
    cnt += 1

    if str(result) == N:
        break

    else:
        int_N = result 

print(cnt)