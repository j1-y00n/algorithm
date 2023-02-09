N = int(input())
room_h = [input() for _ in range(N)]
room_v = [''.join(i) for i in zip(*room_h)]

h_cnt = 0
for h in room_h:
    a = h.split('X')
    for b in a:
        if '..' in b:
            h_cnt += 1

v_cnt = 0
for v in room_v:
    c = v.split('X')
    for d in c:
        if '..' in d:
            v_cnt += 1
               
print(h_cnt, v_cnt)