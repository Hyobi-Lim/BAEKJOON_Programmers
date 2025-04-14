import sys
n,m=map(int,sys.stdin.readline().split())
answer=1
min_num=min(m,n-m)
for i in range(min_num):
    answer*=(n-i)
for i in range(min_num):
    answer//=(i+1)
print(answer)