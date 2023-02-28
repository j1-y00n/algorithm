def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon >= 10:
        eat = coupon//10
        answer += eat
        coupon = coupon%10 + eat
    return answer