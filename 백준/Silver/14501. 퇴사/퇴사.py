import sys
n=int(sys.stdin.readline())
work=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer=0
def work_check(now,work_pay):
    global answer
    if now>=n:
        if answer<work_pay:
            answer=work_pay
        return
    else:
        if now+work[now][0]<=n:
            work_check(now+work[now][0],work_pay+work[now][1])
        work_check(now+1,work_pay)
work_check(0,0)
print(answer)