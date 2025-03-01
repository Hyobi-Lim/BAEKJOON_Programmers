import sys
n,d=map(int,sys.stdin.readline().split())
li=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
shortcut=dict()
answer=d
def find_shortcut(li,now,distance):
    global answer
    if len(li)<=0:
        if answer>distance:
            answer=distance
        return
    else:
        num=0
        for i in range(len(li)):
            if li[i][0]<now:
                num+=1
        if num>=len(li):
            if answer>distance:
                answer=distance
            return
        else:
            newli=li[num+1:]
            find_shortcut(newli,li[num][1],distance-(li[num][1]-li[num][0])+li[num][2])
            find_shortcut(newli,now,distance)
for i in range(len(li)-1,-1,-1):
    if li[i][1]>d:
        li=li[:i]+li[i+1:]
li=sorted(li,key=lambda x:x[0])
find_shortcut(li,0,d)
print(answer)