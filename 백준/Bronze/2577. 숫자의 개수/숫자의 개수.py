A = int(input())
B = int(input())
C = int(input())
t = str(A*B*C)
a = {}
num = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in t:
    c = t.count(i)
    num[i] = c
for j in num.values():
    print(j)