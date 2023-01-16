N = int(input())
score = list(map(int, input().split()))
total = 0
cnt = 0
for i in score:
    if i == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0
print(total)