import sys
from collections import deque
n=int(sys.stdin.readline())
queue=deque()
for i in range(n):
    arr=list(sys.stdin.readline().split())
    if arr[0]=='push':
        queue.append(int(arr[1]))
    elif arr[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif arr[0]=='size':
        print(len(queue))
    elif arr[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif arr[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif arr[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1])