import sys
from collections import deque
n=int(sys.stdin.readline())
tree=dict()
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    if a in tree:
        tree[a].append(b)
    else:
        tree[a]=[b]
    if b in tree:
        tree[b].append(a)
    else:
        tree[b]=[a]
queue=deque([1])
visited=set()
answer=[0]*(n+1)
while(queue):
    now=queue.popleft()
    if now in visited:
        continue
    visited.add(now)
    for i in tree[now]:
        if answer[i]==0:
            answer[i]=now
        if i not in visited:
            queue.append(i)
for i in range(2,len(answer)):
    print(answer[i])