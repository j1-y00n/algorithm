Q = 25
D = 10
N = 5
P = 1

T = int(input())
for _ in range(T):
    C = int(input())
    quarter = C//Q   
    dime = (C - (Q*quarter))//D   
    nickel = (C - (Q*quarter) - (D*dime))//N
    penny = C - (Q*quarter) - (D*dime) - (N*nickel)
    print(quarter, dime, nickel, penny)