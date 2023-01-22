li = [int(input()) for i in range(10)]
li2 = [j % 42 for j in li]
d = {}
for m in li2:
    if m not in d:
        d[m] = 1
    else:
        d[m] += 1
print(len(d))