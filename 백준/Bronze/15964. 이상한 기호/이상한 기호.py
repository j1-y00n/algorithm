def solve(A, B):
    return (A + B) * (A - B)
num = list(map(int, input().split()))
print(solve(A = num[0], B = num[1]))