import sys
t=int(sys.stdin.readline())
for i in range(t):
    n,d=map(int,sys.stdin.readline().split())
    arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    if d==0 or abs(d)==360:
        for j in arr:
            print(*j)
    else:
        if d<0:
            d+=360
        for j in range(d//45):
            temp=[arr[k][n//2] for k in range(n)]
            for k in range(n):
                arr[k][n//2]=arr[k][k]
            new_temp=[arr[n-k-1][k] for k in range(n)]
            for k in range(n):
                arr[k][n-k-1]=temp[k]
            temp=new_temp[:]
            new_temp=arr[n//2][:]
            for k in range(n):
                arr[n//2][k]=temp[k]
            for k in range(n):
                arr[k][k]=new_temp[k]
        for j in arr:
            print(*j)