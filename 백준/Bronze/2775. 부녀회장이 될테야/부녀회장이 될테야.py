T = int(input())
for _ in range(T):
    apt = [['@']*15 for _ in range(15)]
    apt[0] = [a for a in range(15)]
    
    for i in range(1, 15):
        for j in range(15):
            apt[i][j] = sum(apt[i-1][:(j+1)])

    k = int(input())
    n = int(input())
    
    print(apt[k][n])