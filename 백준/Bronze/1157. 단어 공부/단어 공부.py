word = input().upper()
d = {}
for i in word:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

a = sorted(d.items(), key=lambda X : X[1], reverse=True)
if len(a) == 1:
    print(a[0][0])
elif a[0][1] == a[1][1]:
    print("?")
else:
    print(a[0][0])