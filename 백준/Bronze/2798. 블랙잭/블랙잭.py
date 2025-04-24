import sys
n,m=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
answer=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            num=cards[i]+cards[j]+cards[k]
            if num>answer and num<=m:
                answer=num
print(answer)