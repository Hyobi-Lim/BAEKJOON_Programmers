import sys
from collections import deque
n=int(sys.stdin.readline())
ballon_num=[0]+list(map(int,sys.stdin.readline().split()))
ballon=deque(range(2,n+1))
answer=[1]
while(len(ballon)!=0):
    num=ballon_num[answer[len(answer)-1]]
    if num>0:
        for i in range(num):
            now=ballon.popleft()
            if i==num-1:
                answer.append(now)
            else:
                ballon.append(now)
    else:
        for i in range(-num):
            now=ballon.pop()
            if i==-num-1:
                answer.append(now)
            else:
                ballon.appendleft(now)
print(*answer)