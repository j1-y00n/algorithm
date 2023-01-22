num = sorted([int(input()) for i in range(28)])
num2 = [j for j in range(1, 31) if j not in num]
print(*num2, sep = '\n')