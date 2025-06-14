import sys
from collections import deque
n,m,t=map(int,sys.stdin.readline().split())
arr=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
queue=deque([(0,0)])
visited=set()
sword=[0,0]
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            sword=[i,j]
            arr[i][j]=0
            break
while(queue):
    x,y=queue.popleft()
    if (x,y) in visited:
        continue
    visited.add((x,y))
    if 0<=x-1<n and arr[x-1][y]==0:
        arr[x-1][y]=arr[x][y]+1
        queue.append((x-1,y))
    if 0<=x+1<n and arr[x+1][y]==0:
        arr[x+1][y]=arr[x][y]+1
        queue.append((x+1,y))
    if 0<=y-1<m and arr[x][y-1]==0:
        arr[x][y-1]=arr[x][y]+1
        queue.append((x,y-1))
    if 0<=y+1<m and arr[x][y+1]==0:
        arr[x][y+1]=arr[x][y]+1
        queue.append((x,y+1))
answer=arr[n-1][m-1]
if arr[sword[0]][sword[1]]!=0:
    if answer==0:
        answer=arr[sword[0]][sword[1]]+n+m-sword[0]-sword[1]-2
    else:
        answer=min(answer,arr[sword[0]][sword[1]]+n+m-sword[0]-sword[1]-2)
if answer==0 or answer>t:
    print('Fail')
else:
    print(answer)