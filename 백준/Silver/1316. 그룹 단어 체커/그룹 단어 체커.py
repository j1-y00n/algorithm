import sys

N = int(input())
group = N
for _ in range(N):
    word = sys.stdin.readline().strip()

    for i in range(len(word)-1):
        if word[i] != word[i + 1] and word[i] in word[i + 1:]:
            group -= 1
            break
print(group)