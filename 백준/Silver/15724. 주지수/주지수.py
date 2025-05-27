import sys
n,m=map(int,sys.stdin.readline().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))
    for j in range(1,m):
        arr[i][j]+=arr[i][j-1]
    if i!=0:
        for j in range(m):
            arr[i][j]+=arr[i-1][j]
k=int(sys.stdin.readline())
for i in range(k):
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())
    answer=0
    if x1==1 and y1==1:
        answer=arr[x2-1][y2-1]
    elif x1==1:
        answer=arr[x2-1][y2-1]-arr[x2-1][y1-2]
    elif y1==1:
        answer=arr[x2-1][y2-1]-arr[x1-2][y2-1]
    else:
        answer=arr[x2-1][y2-1]-arr[x2-1][y1-2]-arr[x1-2][y2-1]+arr[x1-2][y1-2]
    print(answer)