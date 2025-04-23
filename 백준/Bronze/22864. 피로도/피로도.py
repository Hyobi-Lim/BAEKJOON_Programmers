import sys
a,b,c,m=map(int,sys.stdin.readline().split())
answer=0
fatigue=0
for i in range(24):
    if fatigue+a>m:
        fatigue-=c
        if fatigue<0:
            fatigue=0
    else:
        fatigue+=a
        answer+=b
print(answer)