T = input()
a = T.split('(')
print(a[0].count('@'), a[1].count('@'))