list_1 = []
for i in range(9):
    num = int(input())
    list_1.append(num)
a = max(list_1)    
print(a)
print(list_1.index(a)+1)