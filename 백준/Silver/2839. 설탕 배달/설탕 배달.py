import sys
n=int(sys.stdin.readline())
answer=-1
for i in range(n//5,-1,-1):
    if (n-5*i)%3==0:
        answer+=(i+1)
        answer+=((n-5*i)//3)
        break
print(answer)