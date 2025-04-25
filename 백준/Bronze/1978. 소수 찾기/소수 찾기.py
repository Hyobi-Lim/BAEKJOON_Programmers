import sys
n=int(sys.stdin.readline())
prime=list(map(int,sys.stdin.readline().split()))
answer=0
for i in prime:
    num=0
    for j in range(1,i+1):
        if i%j==0:
            num+=1
    if num==2:
        answer+=1
print(answer)