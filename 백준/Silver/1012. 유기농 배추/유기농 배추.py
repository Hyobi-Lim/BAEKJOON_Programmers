import sys
sys.setrecursionlimit(10**6)
nr=[0,-1,0,1]
nc=[1,0,-1,0]
def dfs(arr,r,c):
    for i in range(4):
        if 0<=r+nr[i]<len(arr) and 0<=c+nc[i]<len(arr[0]) and arr[r+nr[i]][c+nc[i]]==1:
            arr[r+nr[i]][c+nc[i]]=0
            dfs(arr,r+nr[i],c+nc[i])
t=int(sys.stdin.readline())
for i in range(t):
    answer=0
    m,n,k=map(int,sys.stdin.readline().split())
    cabbage=[[0]*m for _ in range(n)]
    for j in range(k):
        x,y=map(int,sys.stdin.readline().split())
        cabbage[y][x]=1
    for a in range(len(cabbage)):
        for b in range(len(cabbage[a])):
            if cabbage[a][b]==1:
                answer+=1
                cabbage[a][b]=0
                dfs(cabbage,a,b)
    print(answer)