import sys

result = 0
A, B = sys.stdin.readline().split()
a = list(A)
B_sum = 0
result= 0

for i in B:
    B_sum += int(i)

for j in a:
    c = int(j)*B_sum
    result += c
print(result)