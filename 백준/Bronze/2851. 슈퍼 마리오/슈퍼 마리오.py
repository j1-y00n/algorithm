li =[]
sum_num = 0
for i in range(10):
    num = int(input())
    sum_num += num
    li.append(sum_num)
li.sort(key= lambda x: abs(x-100))
if abs(100 - li[0]) == abs(100 - li[1]):
    print(li[1])
else:
    print(li[0])