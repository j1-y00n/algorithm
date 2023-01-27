num = [int(input()) for i in range(10)]
s = {j % 42 for j in num}
print(len(s))