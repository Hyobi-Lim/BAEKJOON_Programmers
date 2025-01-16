import sys
sys.setrecursionlimit(10**6)
dr = [0,1,0,-1]
dc = [-1,0,1,0]
def DFS(arr,M,N,num,now):
    count=0
    new_now=[]
    for i in now:
        for j in range(4):
            nr=i[0]+dr[j]
            nc=i[1]+dc[j]
            if nr<0 or nr>=N or nc <0 or nc>=M:
                continue
            if arr[nr][nc]==0:
                arr[nr][nc]=1
                new_now.append([nr,nc])
                count+=1
    if count==0:
        all=[]
        for i in range(N):
            all+=arr[i]
        if 0 in all:
            print(-1)
        else:
            print(num)
        return
    DFS(arr,M,N,num+1,new_now)
M,N=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
now=[]
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            now.append([i,j])
DFS(arr,M,N,0,now)