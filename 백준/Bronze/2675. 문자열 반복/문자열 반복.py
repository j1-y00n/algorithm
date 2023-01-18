T = int(input())
for i in range(T):
    R, S = input().split()
    result = [int(R)*j for j in S]
    print(''.join(result))