import sys
n,m=map(int,sys.stdin.readline().split())
s=set()
for i in range(n):
    str=sys.stdin.readline().strip()
    s.add(str)
answer=0
for i in range(m):
    str=sys.stdin.readline().strip()
    if str in s:
        answer+=1
print(answer)