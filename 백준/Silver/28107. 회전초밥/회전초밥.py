import sys
sys.setrecursionlimit(10**6)
n,m=map(int,sys.stdin.readline().split())
people=[0]*n
sushi_waiting=dict()
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(arr)):
        if arr[j] in sushi_waiting:
            sushi_waiting[arr[j]].append(i)
        else:
            sushi_waiting[arr[j]]=[i]
sushi=list(map(int,sys.stdin.readline().split()))
for i in sushi:
    if i in sushi_waiting:
        num=sushi_waiting[i].pop(0)
        if len(sushi_waiting[i])==0:
            del sushi_waiting[i]
        people[num]+=1
for i in people:
    print(i,end=' ')