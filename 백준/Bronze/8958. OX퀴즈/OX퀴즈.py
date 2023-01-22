T = int(input())
for t in range(T):
    cnt = 0
    result = 0
    ox = input()
    for i in ox:
        if i == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)