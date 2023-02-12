import sys

direct = {
    "R": (0, 1),
    "L": (0, -1),
    "T": (-1, 0),
    "B": (1, 0),
    "RT": (-1, 1),
    "RB": (1, 1),
    "LT": (-1, -1),
    "LB": (1, -1),
}

K, S, N = sys.stdin.readline().split()
kx = 8 - int(K[1])
ky = "ABCDEFGH".index(K[0])
sx = 8 - int(S[1])
sy = "ABCDEFGH".index(S[0])

li= [sys.stdin.readline().strip() for _ in range(int(N))]

for i in li:
    dx = kx + direct[i][0]
    dy = ky + direct[i][1]
    
    if 0 <= dx < 8 and 0 <= dy <8:
        if dx == sx and dy == sy:
            nx = sx + direct[i][0]
            ny = sy + direct[i][1]
            if 0 <= nx < 8 and 0 <= ny <8:
                kx = dx
                ky = dy
                sx = nx
                sy = ny      
        else:
            kx = dx
            ky = dy

print(f'{"ABCDEFGH"[ky]}{8 - kx}')
print(f'{"ABCDEFGH"[sy]}{8 - sx}')