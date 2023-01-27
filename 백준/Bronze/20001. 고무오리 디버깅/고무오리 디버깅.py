start = input()
li = []
while True:
    words = input()
    if words == '문제':
        li.append(words)
    elif words == '고무오리':
        if li:
            li.pop()
        else:
            li.append('문제')
            li.append('문제')
    elif words == '고무오리 디버깅 끝':
        break

if len(li) == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')