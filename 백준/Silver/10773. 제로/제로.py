K = int(input())
li = []
for _ in range(K):
    num = int(input())
    if num != 0:
        li.append(num)
    else:
        li.pop()
print(sum(li))