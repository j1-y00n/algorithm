word = input()
a = []
for i in word:
    if i not in 'CAMBRIDGE':
        a.append(i)
print(''.join(a))
