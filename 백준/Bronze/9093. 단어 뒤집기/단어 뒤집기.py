T = int(input())
for t in range(T):
    sen = input().split()
    sen_list = []
    for i in sen:
        sen_list.append(i[::-1])
    print(*sen_list)