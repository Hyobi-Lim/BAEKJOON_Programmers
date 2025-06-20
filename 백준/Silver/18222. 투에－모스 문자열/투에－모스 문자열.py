import sys
n=int(sys.stdin.readline())
n-=1
n=list(bin(n)[2:])
cnt=0
for i in n:
    if i=='1':
        cnt+=1
if cnt%2==0:
    print(0)
else:
    print(1)