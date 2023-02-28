def solution(price, money, count):
    a = 0
    for i in range(1, count + 1):
        a += (i * price)
    if money - a < 0:
        return -(money - a)
    
    return 0