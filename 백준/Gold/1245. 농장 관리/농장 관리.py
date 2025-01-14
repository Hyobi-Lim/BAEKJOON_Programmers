import sys
sys.setrecursionlimit(10**6)
answer=0
dr = [-1,-1,-1,0,0,1,1,1]
dc = [-1,0,1,-1,1,-1,0,1]
def DFS(r,c,a,b):
    num=arr[r][c]
    arr[r][c] = -1
    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nr>=a or nc <0 or nc>=b:
            continue
        if arr[nr][nc] == -1 or arr[nr][nc]>num:
            continue
        DFS(nr,nc,a,b)
a, b = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(a)]
while(max(map(max, arr))!=-1):
    num=max(map(max, arr))
    for i in range(a):
        for j in range(b):
            if arr[i][j] == num:
                answer+=1
                DFS(i,j,a,b)
print(answer)