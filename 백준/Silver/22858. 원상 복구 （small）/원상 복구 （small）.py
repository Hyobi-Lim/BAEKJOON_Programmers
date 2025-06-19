import sys
n,k=map(int,sys.stdin.readline().split())
s=list(map(int,sys.stdin.readline().split()))
d=list(map(int,sys.stdin.readline().split()))
answer=[0]*n
for i in range(k):
    for j in range(n):
        answer[d[j]-1]=s[j]
    s=answer[:]
print(*answer)