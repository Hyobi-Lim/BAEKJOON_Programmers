import sys
n=int(sys.stdin.readline())
now=1
answer=0
while(now<n):
    if now+sum(map(int,str(now)))==n:
        answer=now
        break
    now+=1
print(answer)