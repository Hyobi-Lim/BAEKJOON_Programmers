import sys
sys.setrecursionlimit(10**9)
from copy import deepcopy
num=int(input())
all=[input().strip() for _ in range(num)]
arr=[list(line) for line in all]
abarr=deepcopy(arr)
normal=0
abnormal=0
def normal_check(arr,alp,num,n,c):
    nr=[-1,0,1,0]
    nc=[0,1,0,-1]
    for i in range(4):
        if 0<=n+nr[i]<num and 0<=c+nc[i]<num and arr[n+nr[i]][c+nc[i]]==alp:
            arr[n+nr[i]][c+nc[i]]='0'
            normal_check(arr,alp,num,n+nr[i],c+nc[i])
for i in range(num):
    for j in range(num):
        if abarr[i][j]=='G':
            abarr[i][j]='R'
for i in range(num):
    for j in range(num):
        if arr[i][j]!='0':
            normal_check(arr,arr[i][j],num,i,j)
            normal+=1
        if abarr[i][j]!='0':
            normal_check(abarr,abarr[i][j],num,i,j)
            abnormal+=1
print(normal,abnormal)