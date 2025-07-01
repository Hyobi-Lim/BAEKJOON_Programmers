import sys
from collections import deque
m,n,h=map(int,sys.stdin.readline().split())
tomato=[[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
queue=deque()
zero_cnt=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                queue.append([i,j,k])
            elif tomato[i][j][k]==0:
                zero_cnt+=1
if zero_cnt==0:
    print(0)
else:
    visited=set()
    answer=0
    while(queue):
        answer+=1
        new_queue=deque()
        while(queue):
            a,b,c=queue.popleft()
            if (a,b,c) in visited:
                continue
            visited.add((a,b,c))
            if 0<=a-1<h and tomato[a-1][b][c]==0:
                tomato[a-1][b][c]=1
                new_queue.append((a-1,b,c))
            if 0<=a+1<h and tomato[a+1][b][c]==0:
                tomato[a+1][b][c]=1
                new_queue.append((a+1,b,c))
            if 0<=b-1<n and tomato[a][b-1][c]==0:
                tomato[a][b-1][c]=1
                new_queue.append((a,b-1,c))
            if 0<=b+1<n and tomato[a][b+1][c]==0:
                tomato[a][b+1][c]=1
                new_queue.append((a,b+1,c))
            if 0<=c-1<m and tomato[a][b][c-1]==0:
                tomato[a][b][c-1]=1
                new_queue.append((a,b,c-1))
            if 0<=c+1<m and tomato[a][b][c+1]==0:
                tomato[a][b][c+1]=1
                new_queue.append((a,b,c+1))
        queue=new_queue
    answer-=1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k]==0:
                    answer=-1
    print(answer)