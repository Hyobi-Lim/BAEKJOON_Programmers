import sys
n,k=map(int,sys.stdin.readline().split())
bag=[]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    bag.append((w,v))
dp=[0]*(k+1)
for w,v in bag:
    for weight in range(k,w-1,-1):
        dp[weight]=max(dp[weight],dp[weight-w]+v)
print(dp[k])