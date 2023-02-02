import sys

W = [int(sys.stdin.readline().strip()) for _ in range(10)]

K = [int(sys.stdin.readline().strip()) for _ in range(10)]

W2, K2 = sorted(W), sorted(K)

print(sum(W2[7:10]), sum(K2[7:10]))
