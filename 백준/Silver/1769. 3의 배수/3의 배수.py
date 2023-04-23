X = input()
Y = X
cnt = 0

def A(a):
    global Y
    y = 0
    for i in str(a):
        y += int(i)
        Y = y

while True:
    if len(str(Y)) == 1:
        break
    else:
        A(Y)
        cnt += 1

print(cnt)
if int(Y) in [3, 6, 9]:
    print('YES')
else:
    print('NO')