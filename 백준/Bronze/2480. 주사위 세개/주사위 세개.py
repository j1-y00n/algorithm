a, b, c = list(map(int, input().split()))
if a == b:
    if a == c:
        print(10000 + a * 1000)
    else :
        print(1000 + a * 100)

elif a == c:
    if a == b:
        print(10000 + a * 1000)
    else :
        print(1000 + a * 100)

elif b == c:
    if b == a:
        print(10000 + b * 1000)
    else :
        print(1000 + b * 100)
 
else:
    print(max(a, b, c) * 100)
