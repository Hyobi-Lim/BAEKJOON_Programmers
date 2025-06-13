import sys
n=int(sys.stdin.readline())
house=[list(sys.stdin.readline().strip()) for _ in range(n)]
cnt=0
def dfs(x,y):
    global cnt
    house[x][y]='0'
    cnt+=1
    if 0<=x-1<n and house[x-1][y]=='1':
        dfs(x-1,y)
    if 0<=y-1<n and house[x][y-1]=='1':
        dfs(x,y-1)
    if 0<=x+1<n and house[x+1][y]=='1':
        dfs(x+1,y)
    if 0<=y+1<n and house[x][y+1]=='1':
        dfs(x,y+1)
answer=[]
for i in range(n):
    for j in range(n):
        if house[i][j]=='1':
            cnt=0
            dfs(i,j)
            answer.append(cnt)
answer.sort()
print(len(answer))
for i in answer:
    print(i)