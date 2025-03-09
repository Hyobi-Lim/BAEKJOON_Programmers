import sys
from collections import deque
answer=0
n,m=map(int,sys.stdin.readline().split())
edges=[[] for _ in range(n+1)]
for i in range(m):
    answer=0
    u,v=map(int,sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)
queue=deque()
visited=set()
for i in range(1,n+1):
    if i not in visited:
        answer+=1
        queue.append(i)
        while queue:
            now=queue.popleft()
            if now not in visited:
                visited.add(now)
                for j in edges[now]:
                    if j not in visited:
                        queue.append(j)
print(answer)