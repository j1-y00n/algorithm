import sys


while True:
    num = sys.stdin.readline().strip()
    l_num = len(num)
    half_num = int(len(num)/2)

    if num == '0':
        break
    
    if num[0:half_num] == num[l_num - 1:l_num - 1 - half_num:-1]:
         print('yes')
         
    else:
        print('no')