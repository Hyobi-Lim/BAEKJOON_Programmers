import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
target=int(sys.stdin.readline())
sq=0
while(n!=2**sq):
    sq+=1
for i in range(1,sq+1):
    for j in range(n//2**i):
        arr[j*2**i:(j+1)*2**i]=sorted(arr[j*2**i:(j+1)*2**i])
    if n//2**i==target:
        break
for i in range(n):
    print(arr[i],end=' ')