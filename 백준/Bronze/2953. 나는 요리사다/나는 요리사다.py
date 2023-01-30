li = [(sum(list(map(int, input().split()))), i) for i in range(1, 6)]
print(f'{max(li)[1]} {max(li)[0]}')