import sys
n,m=map(int,sys.stdin.readline().split())
s=set()
answer=0
for i in range(n):
    str=sys.stdin.readline().strip()
    for j in range(1,len(str)+1):
        s.add(str[:j])
for i in range(m):
    str=sys.stdin.readline().strip()
    if str in s:
        answer+=1
print(answer)