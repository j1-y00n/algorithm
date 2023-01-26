N = int(input())
li = []
cnt = 0
guest = list(map(int, input().split()))
for i in guest:
    if i not in li:
        li.append(i)
    else:
        cnt += 1
print(cnt)