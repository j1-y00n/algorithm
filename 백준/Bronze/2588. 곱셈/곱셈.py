a = int(input())
b = list(input())
c = list(map(int,b))
i = a*c[2]
j = a*c[1]
k = a*c[0]
print(i, j, k, i+(j*10)+(k*100), sep ='\n')
