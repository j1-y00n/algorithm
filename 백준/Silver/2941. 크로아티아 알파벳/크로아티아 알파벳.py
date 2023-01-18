word = input()
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in li:
    word = word.replace(i, '@')
print(len(word))