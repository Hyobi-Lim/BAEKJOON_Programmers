import sys
from collections import deque
n=int(sys.stdin.readline())
child=[[] for _ in range(n)]
parent=list(map(int,sys.stdin.readline().split()))
root=0
for i in range(n):
    now=parent[i]
    if parent[i]==-1:
        root=i
    else:
        child[now].append(i)
remove_node=int(sys.stdin.readline())
queue=deque([root])
answer=0
if root!=remove_node:
    while(queue):
        now=queue.popleft()
        if child[now]==[remove_node] or child[now]==[]:
            answer+=1
        else:
            for i in child[now]:
                if i!=remove_node:
                    queue.append(i)
print(answer)