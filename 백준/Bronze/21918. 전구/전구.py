import sys
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if a==1:
        arr[b-1]=c
    elif a==2:
        for j in range(b-1,c):
            if arr[j]==0:
                arr[j]=1
            else:
                arr[j]=0
    elif a==3:
        for j in range(b-1,c):
            arr[j]=0
    else:
        for j in range(b-1,c):
            arr[j]=1
print(*arr)