T = int(input())
for _ in range(T):
    PS = input()
    while "()" in PS:
        PS = PS.replace("()", "")
    if len(PS) == 0:
        print("YES")
    else:
        print("NO")