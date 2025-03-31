import sys,math,heapq
n,m=map(int,sys.stdin.readline().split())
nexus=list(map(int,sys.stdin.readline().split()))
nexuscheck=set()
route=dict()
for i in range(n):
    if i!=n-1 and nexus[i]==1:
        nexuscheck.add(i)
    route[i]=[]
for i in range(m):
    a,b,t=map(int,sys.stdin.readline().split())
    if a in nexuscheck or b in nexuscheck:
        continue
    else:
        route[a].append((b,t))
        route[b].append((a,t))
time=[math.inf]*n
time[0]=0
visited=set()
heap=[]
heapq.heappush(heap,(0,0))
while heap:
    nowtime,node=heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)
    for i in route[node]:
        if nowtime+i[1]<time[i[0]]:
            time[i[0]]=nowtime+i[1]
            heapq.heappush(heap,(time[i[0]],i[0]))
if time[n-1]==math.inf:
    print(-1)
else:
    print(time[n-1])