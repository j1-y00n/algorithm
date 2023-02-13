def Rev(X, Y):
    a = int(X[::-1]) + int(Y[::-1])
    return int(str(a)[::-1])

x, y = input().split()
print(Rev(x, y))