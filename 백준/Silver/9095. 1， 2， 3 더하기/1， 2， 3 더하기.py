import sys
def one_two_three(now_sum,now_num):
    global answer
    if now_sum==now_num:
        answer+=1
        return
    else:
        if now_sum+1<=now_num:
            one_two_three(now_sum+1,now_num)
        if now_sum+2<=now_num:
            one_two_three(now_sum+2,now_num)
        if now_sum+3<=now_num:
            one_two_three(now_sum+3,now_num)
n=int(sys.stdin.readline())
answer=0
for i in range(n):
    num=int(sys.stdin.readline())
    answer=0
    one_two_three(0,num)
    print(answer)