import sys
from itertools import product
n,k=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
answer=arr[len(arr)-1]
for i in range(len(arr)):
    arr[i]=str(arr[i])
num=1
check=True
while(check):
    for i in product(arr,repeat=num):
        if int(''.join(i))<=n:
            answer=int(''.join(i))
        else:
            check=False
            break
    num+=1
print(answer)