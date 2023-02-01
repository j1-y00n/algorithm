N = int(input())
for i in range(N, 3, -1):
    li = []
    for s in str(i):
        li.append(s == '4' or s == '7')
    if all(li):
        print(i)
        break