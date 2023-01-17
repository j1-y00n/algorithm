A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
list_1 = [A[0], B[0], C[0]]
list_2 = [A[1], B[1], C[1]]
s1 = set(list_1)
s2 = set(list_2)
print((sum(s1)*2)-sum(list_1), (sum(s2)*2)-sum(list_2))