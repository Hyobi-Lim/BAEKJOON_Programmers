import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
josephus=deque(range(1,n+1))
answer=[]
while (len(josephus)!=0):
    for i in range(k-1):
        josephus.append(josephus.popleft())
    answer.append(josephus.popleft())
print("<",end="")
for i in range(len(answer)):
    if i==len(answer)-1:
        print(answer[i],end="")
    else:
        print(answer[i],end=", ")
print(">")