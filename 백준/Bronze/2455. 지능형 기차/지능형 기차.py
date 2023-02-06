import sys

people = [list(map(int, input().split())) for _ in range(4)]

max_people = 0
num = people[0][1]
for i in range(1, 4):
    num = num - people[i][0] + people[i][1]
    if max_people < num:
        max_people = num
print(max_people)