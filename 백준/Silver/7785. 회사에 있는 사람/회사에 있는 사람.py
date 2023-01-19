n = int(input())
name = {}
name2 = []
for i in range(n):
    a, b = input().split()
    name[a] = b
for j in name:
    if name[j] == 'enter':
        name2.append(j)
print(*sorted(name2, reverse = True), sep = '\n')