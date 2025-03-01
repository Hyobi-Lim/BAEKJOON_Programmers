import sys
sys.setrecursionlimit(10**9)
n,m=map(int,sys.stdin.readline().split())
li=[list(sys.stdin.readline().strip()) for _ in range(n)]
def find_way(li,r,c,count):
    dr=[0,1,0,-1]
    dc=[1,0,-1,0]
    q=[]
    q.append((r,c))
    li[r][c]=1
    while q:
        nowr,nowc=q.pop(0)
        for i in range(4):
            nr=nowr+dr[i]
            nc=nowc++dc[i]
            if 0<=nr<n and 0<=nc<m and li[nr][nc]=='1':
                q.append((nr,nc))
                li[nr][nc]=li[nowr][nowc]+1

find_way(li,0,0,1)
print(li[n-1][m-1])