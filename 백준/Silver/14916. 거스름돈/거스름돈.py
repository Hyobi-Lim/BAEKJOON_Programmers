import sys
n=int(sys.stdin.readline())
answer=-1
for i in range(n//5,-1,-1):
    if (n-5*i)%2==0:
        answer=i+(n-5*i)//2
        break
print(answer)