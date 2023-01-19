num = [int(input()) for i in range(7)]
num2 = []

for j in num:
    if j % 2 == 1:
        num2.append(j)
if len(num2) == 0:
    print(-1)
else:
    print(sum(num2), min(num2), sep = '\n')