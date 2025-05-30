import sys
switch=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
t=int(sys.stdin.readline())
for i in range(t):
    sex,now=map(int,sys.stdin.readline().split())
    if sex==1:
        for j in range(now-1,switch,now):
            arr[j]=1-arr[j]
    else:
        arr[now-1]=1-arr[now-1]
        left=now-2
        right=now
        while(left>=0 and right<switch):
            if arr[left]==arr[right]:
                arr[left]=1-arr[left]
                arr[right]=1-arr[right]
                left-=1
                right+=1
            else:
                break
for i in range(0,switch,20):
    print(*arr[i:i+20])