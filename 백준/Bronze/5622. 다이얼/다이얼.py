a = input()
b = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 
    'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}
t = 0
for i in a:
    for k, v in b.items():
        if i in k:
            t += v
print(t)