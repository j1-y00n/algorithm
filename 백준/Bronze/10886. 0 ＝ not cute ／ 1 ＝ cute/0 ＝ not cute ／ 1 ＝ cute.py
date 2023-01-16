people = int(input())
a = []
for p in range(people):
    i = int(input())
    a.append(i)

if a.count(0) > a.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')