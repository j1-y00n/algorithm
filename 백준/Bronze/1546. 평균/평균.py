N = int(input())
score = list(map(int, input().split()))
# a = sum(score)/len(score)
M = max(score)
score2 = [i/M*100 for i in score]
print(sum(score2)/N)