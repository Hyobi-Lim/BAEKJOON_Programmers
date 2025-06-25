import sys
from itertools import permutations
n=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    arr[i][0]=[arr[i][0]//100,arr[i][0]%100//10,arr[i][0]%10]
answer=0
for i in permutations([1,2,3,4,5,6,7,8,9],3):
    cnt=0
    for j in arr:
        strike=0
        ball=0
        if j[0][0]==i[0]:
            strike+=1
        else:
            if j[0][0] in i:
                ball+=1
        if j[0][1]==i[1]:
            strike+=1
        else:
            if j[0][1] in i:
                ball+=1
        if j[0][2]==i[2]:
            strike+=1
        else:
            if j[0][2] in i:
                ball+=1
        if strike==j[1] and ball==j[2]:
            cnt+=1
    if cnt==n:
        answer+=1
print(answer)