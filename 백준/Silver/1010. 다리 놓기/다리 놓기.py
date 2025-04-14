import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    answer=1
    min_num=min(n,m-n)
    for j in range(min_num):
        answer*=(m-j)
    for j in range(min_num):
        answer//=(j+1)
    print(answer)