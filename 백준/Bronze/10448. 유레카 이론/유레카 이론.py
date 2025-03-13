import sys
sys.setrecursionlimit(10**6)
def eureka(target,t1):
    global answer
    for i in range(t1,0,-1):
        for j in range(i,0,-1):
            if target==(t1*(t1+1)+i*(i+1)+j*(j+1))//2:
                answer=1
                return
    if target<(t1*(t1+1)+4)//2:
        return
    eureka(target,t1+1)
n=int(sys.stdin.readline())
for i in range(n):
    answer=0
    target=int(sys.stdin.readline())
    eureka(target,1)
    print(answer)