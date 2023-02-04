import sys

group = 0
N = int(input())
for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) == 1:
        group += 1
    
    else:
        check = []
        w = word[0]
        for i in range(1, len(word)):
            if w != word[i]:
                check.append(w)
                w = word[i]
        check.append(word[i])
        
        s_word = set(word)
        if len(check) == len(s_word):
            group += 1

print(group)