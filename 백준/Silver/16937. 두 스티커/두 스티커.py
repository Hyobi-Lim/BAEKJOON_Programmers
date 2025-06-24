import sys
h,w=map(int,sys.stdin.readline().split())
if h<w:
    h,w=w,h
n=int(sys.stdin.readline())
sticker=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    if sticker[i][0]<sticker[i][1]:
        sticker[i][0],sticker[i][1]=sticker[i][1],sticker[i][0]
answer=0
for i in range(n-1):
    for j in range(i+1,n):
        x1,y1=sticker[i]
        x2,y2=sticker[j]
        if max(max(x1,x2),y1+y2)<=h and min(max(x1,x2),y1+y2)<=w:
            if answer==0 or answer<x1*y1+x2*y2:
                answer=x1*y1+x2*y2
        if max(x1+x2,max(y1,y2))<=h and min(x1+x2,max(y1,y2))<=w:
            if answer==0 or answer<x1*y1+x2*y2:
                answer=x1*y1+x2*y2
        if max(x1+y2,max(x2,y1))<=h and min(x1+y2,max(x2,y1))<=w:
            if answer==0 or answer<x1*y1+x2*y2:
                answer=x1*y1+x2*y2
        if max(max(x1,y2),x2+y1)<=h and min(max(x1,y2),x2+y1)<=w:
            if answer==0 or answer<x1*y1+x2*y2:
                answer=x1*y1+x2*y2
print(answer)