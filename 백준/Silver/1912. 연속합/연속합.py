import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
answer=arr[0]
now_max=arr[0]
for i in range(1,n):
    now_max=max(now_max+arr[i],arr[i])
    answer=max(answer,now_max)
print(answer)