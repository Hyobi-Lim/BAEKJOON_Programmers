import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
arr=[list(map(int,input().split())) for _ in range(n)]
x,y=0,0
for i in range(n):
    for j in range(m):
        if arr[i][j]==2:
            x,y=i,j
queue=deque([[x,y]])
visited=set()
while(queue):
    now_x,now_y=queue.popleft()
    if (now_x,now_y) in visited:
        continue
    visited.add((now_x,now_y))
    if 0<=now_x-1<n and arr[now_x-1][now_y]==1:
        queue.append([now_x-1,now_y])
        arr[now_x-1][now_y]=arr[now_x][now_y]+1
    if 0<=now_y-1<m and arr[now_x][now_y-1]==1:
        queue.append([now_x,now_y-1])
        arr[now_x][now_y-1]=arr[now_x][now_y]+1
    if 0<=now_x+1<n and arr[now_x+1][now_y]==1:
        queue.append([now_x+1,now_y])
        arr[now_x+1][now_y]=arr[now_x][now_y]+1
    if 0<=now_y+1<m and arr[now_x][now_y+1]==1:
        queue.append([now_x,now_y+1])
        arr[now_x][now_y+1]=arr[now_x][now_y]+1
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            arr[i][j]=-1
        elif arr[i][j]!=0:
            arr[i][j]-=2
for i in range(n):
    print(*arr[i])