import sys
from collections import deque
r1,c1=map(int,sys.stdin.readline().split())
r2,c2=map(int,sys.stdin.readline().split())
dr1=[0,-1,0,1]
dc1=[-1,0,1,0]
dr2=[[1,-1],[-1,-1],[-1,1],[1,1]]
dc2=[[-1,-1],[-1,1],[1,1],[1,-1]]
visited=set()
visitedcount=dict()
queue=deque()
queue.append((r1,c1))
visitedcount[(r1,c1)]=0
while(queue):
    now=queue.popleft()
    if now not in visited:
        visited.add(now)
        for i in range(4):
            for j in range(2):
                if 0<=now[0]+dr1[i]+dr2[i][j]*2<=9 and 0<=now[1]+dc1[i]+dc2[i][j]*2<=8 and (now[0]+dr1[i]+dr2[i][j]*2,now[1]+dc1[i]+dc2[i][j]*2) not in visited and (r2,c2) not in ((now[0]+dr1[i],now[1]+dc1[i]),(now[0]+dr1[i]+dr2[i][j],now[1]+dc1[i]+dc2[i][j])):
                    queue.append((now[0]+dr1[i]+dr2[i][j]*2,now[1]+dc1[i]+dc2[i][j]*2))
                    visitedcount[(now[0]+dr1[i]+dr2[i][j]*2,now[1]+dc1[i]+dc2[i][j]*2)]=visitedcount[(now[0],now[1])]+1
    if (r2,c2) in visitedcount:
        break
if (r2,c2) in visitedcount:
    print(visitedcount[(r2,c2)])
else:
    print(-1)