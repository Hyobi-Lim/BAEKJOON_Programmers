import sys
n=int(sys.stdin.readline())
str=sys.stdin.readline().strip()
str=list(str)
rb=dict()
rb['R']=0
rb['B']=0
answer=0
for i in str:
    if i=='R':
        rb['R']+=1
    else:
        rb['B']+=1
if rb['R']==0 or rb['B']==0:
    print(answer)
else:
    ball_count=[0,0,0,0]
    for i in range(len(str)-1,-1,-1):
        if str[i]=='B':
            ball_count[0]=rb['R']-len(str)+1+i
            break
    for i in range(len(str)):
        if str[i]=='R':
            ball_count[1]=rb['B']-i
            break
    for i in range(len(str)-1,-1,-1):
        if str[i]=='R':
            ball_count[2]=rb['B']-len(str)+1+i
            break
    for i in range(len(str)):
        if str[i]=='B':
            ball_count[3]=rb['R']-i
            break
    print(min(ball_count))