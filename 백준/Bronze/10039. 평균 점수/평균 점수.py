A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
score1 = [A, B, C, D, E]
score2 = []
for i in score1:
    if i < 40:
        score2.append(40)
    else:
        score2.append(i)
print(int((sum(score2))/5))