import sys
from collections import deque
n,m,v=map(int,sys.stdin.readline().split())
edges=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)
for i in range(1,n+1):
    edges[i].sort()
queue=deque()
queue.append(v)
visited=[]
while queue:
    now=queue.popleft()
    if now not in visited:
        visited.append(now)
        for i in range(len(edges[now])-1,-1,-1):
            if edges[now][i] not in visited:
                queue.appendleft(edges[now][i])
for i in visited:
    print(i,end=' ')
print()
queue=deque()
queue.append(v)
visited=[]
while queue:
    now=queue.popleft()
    if now not in visited:
        visited.append(now)
        for i in edges[now]:
            if i not in visited:
                queue.append(i)
for i in visited:
    print(i,end=' ')