import sys
from collections import deque
num=int(sys.stdin.readline())
for i in range(num):
    n,m=map(int,sys.stdin.readline().split())
    arr=list(map(int,sys.stdin.readline().split()))
    max=arr[:]
    max.sort()
    arr=deque(arr)
    for j in range(len(arr)):
        arr[j]=[j,arr[j]]
    if n==1:
        print(1)
    else:
        answer=[]
        while(1):
            if arr[0][1]==max[len(max)-1]:
                answer.append(arr.popleft())
                max.pop()
            else:
                arr.append(arr.popleft())
            if len(answer)!=0 and answer[len(answer)-1][0]==m:
                break
        print(len(answer))