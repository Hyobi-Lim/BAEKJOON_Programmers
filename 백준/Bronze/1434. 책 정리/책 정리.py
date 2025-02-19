import sys
n,m=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))
now_box_index=0
for i in range(m):
    while(b[i]!=0):
        if a[now_box_index]>=b[i]:
            a[now_box_index]-=b[i]
            b[i]=0
            break
        else:
            now_box_index+=1
print(sum(a))