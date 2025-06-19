import sys
n,m=map(int,sys.stdin.readline().split())
train=[[0]*20 for _ in range(n)]
for i in range(m):
    arr=list(map(int,sys.stdin.readline().split()))
    if arr[0]==1:
        train[arr[1]-1][arr[2]-1]=1
    elif arr[0]==2:
        train[arr[1]-1][arr[2]-1]=0
    elif arr[0]==3:
        for j in range(19,0,-1):
            train[arr[1]-1][j]=train[arr[1]-1][j-1]
        train[arr[1]-1][0]=0
    else:
        for j in range(19):
            train[arr[1]-1][j]=train[arr[1]-1][j+1]
        train[arr[1]-1][19]=0
train_set=set()
for i in range(n):
    train_set.add(tuple(train[i]))
print(len(train_set))