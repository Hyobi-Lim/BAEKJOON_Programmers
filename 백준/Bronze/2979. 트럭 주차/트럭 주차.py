import sys
a,b,c=map(int,sys.stdin.readline().split())
time=dict()
for i in range(3):
    timein,timeout=map(int,sys.stdin.readline().split())
    for j in range(timein,timeout):
        if j in time:
            time[j]+=1
        else:
            time[j]=1
answer=0
for i in time:
    if time[i]==1:
        answer+=a
    elif time[i]==2:
        answer+=(b*2)
    else:
        answer+=(c*3)
print(answer)