import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
coins=[]
all_coins=deque()
answer=[0]*(m+1)
for i in range(n):
    now=int(sys.stdin.readline())
    if now<=m and now not in coins:
        coins.append(now)
        all_coins.append(now)
        answer[now]=1
if len(coins)==1:
    if m%coins[0]==0:
        print(m//coins[0])
    else:
        print(-1)
else:
    coins.sort()
    while all_coins:
        if answer[m]!=0:
            print(answer[m])
            break
        now=all_coins.popleft()
        for i in coins:
            if now+i>m:
                break
            if answer[now+i]!=0:
                continue
            elif now+i==m:
                answer[now+i]=answer[now]+1
                break
            elif now+i<m:
                answer[now+i]=answer[now]+1
                all_coins.append(now+i)
    if answer[m]==0:
        print(-1)