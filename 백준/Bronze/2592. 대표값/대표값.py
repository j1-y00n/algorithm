import sys

d = {}
num = [int(sys.stdin. readline()) for _ in range(10)]
for i in num:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
d1 = sorted(d.items(), key=lambda x: x[1], reverse= True)
print(int(sum(num)/10))
print(d1[0][0])