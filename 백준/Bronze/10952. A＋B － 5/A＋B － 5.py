A, B = list(map(int, input().split()))
while A and B > 0:
    print(A+B)
    A, B = list(map(int, input().split()))
    if A and B == 0:
        break