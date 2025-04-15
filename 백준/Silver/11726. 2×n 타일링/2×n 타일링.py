import sys
n=int(sys.stdin.readline())
answer=1
for i in range(1,n//2+1):
    now=1
    min_now=min(i,n-2*i)
    for j in range(min_now):
        now*=(n-i-j)
    for j in range(min_now):
        now//=(j+1)
    answer+=now
    answer%=10007
print(answer)