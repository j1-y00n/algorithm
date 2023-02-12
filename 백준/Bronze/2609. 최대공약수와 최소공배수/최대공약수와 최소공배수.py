x, y = list(map(int, input().split()))
li1 = []
li2 = []
for i in range(1, x + 1):
    if x % i == 0:
        li1.append(i)
for j in range(1, y + 1):
    if y % j == 0:
        li2.append(j)

result = sorted(list(set(li1)&set(li2)))[-1]
a , b = x/result, y/result
print(result, int(result * a * b), sep='\n')