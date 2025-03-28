import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
eggs=[]
for i in range(n):
    s,w=map(int,sys.stdin.readline().split())
    eggs.append([s,w])
answer=0
def alleggs(eggs,now):
    global answer
    if now>=n:
        count=0
        for i in eggs:
            if i[0]<=0:
                count+=1
        if answer<count:
            answer=count
        return
    else:
        if eggs[now][0]<=0:
            alleggs(eggs,now+1)
        else:
            minuscount=0
            for i in range(len(eggs)):
                if i!=now and eggs[i][0]>0:
                    minuscount+=1
                    eggs[now][0]-=eggs[i][1]
                    eggs[i][0]-=eggs[now][1]
                    alleggs(eggs,now+1)
                    eggs[now][0]+=eggs[i][1]
                    eggs[i][0]+=eggs[now][1]
            if minuscount==0:
                count=0
                for i in eggs:
                    if i[0]<=0:
                        count+=1
                if answer<count:
                    answer=count
                return
alleggs(eggs,0)
print(answer)