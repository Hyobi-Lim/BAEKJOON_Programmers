import sys
from itertools import permutations
n=int(sys.stdin.readline())
number=list(map(int,sys.stdin.readline().split()))
operator_num=list(map(int,sys.stdin.readline().split()))
operator=['+']*operator_num[0]+['-']*operator_num[1]+['×']*operator_num[2]+['÷']*operator_num[3]
operator_set=set()
for i in permutations(operator,n-1):
        operator_set.add(i)
max_num=-1000000000
min_num=1000000000
for i in operator_set:
    num=number[0]
    for j in range(n-1):
        if i[j]=='+':
            num+=number[j+1]
        elif i[j]=='-':
            num-=number[j+1]
        elif i[j]=='×':
            num*=number[j+1]
        else:
            if num*number[j+1]<=0:
                num=abs(num)//abs(number[j+1])*-1
            else:
                num//=number[j+1]
    if max_num<num:
        max_num=num
    if min_num>num:
        min_num=num
print(max_num)
print(min_num)