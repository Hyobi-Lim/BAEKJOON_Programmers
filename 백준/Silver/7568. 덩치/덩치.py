import sys
n=int(sys.stdin.readline())
xy=[]
rank=[]
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    xy.append(arr)
for i in range(n):
    nowrank=1
    for j in range(n):
        if xy[j][0]>xy[i][0] and xy[j][1]>xy[i][1]:
            nowrank+=1
    rank.append(nowrank)
for i in range(n):
    print(rank[i],end=' ')