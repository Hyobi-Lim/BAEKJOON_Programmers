import sys
r,c,n=map(int,sys.stdin.readline().split())
arr=[list(sys.stdin.readline().strip()) for _ in range(r)]
if n%2==0:
    for i in range(r):
        print('O'*c)
else:
    bomb=set()
    for i in range(1,n):
        if i%2==1:
            bomb=set()
            for j in range(r):
                for k in range(c):
                    if arr[j][k]=='O':
                        bomb.add((j,k))
                        if 0<=j-1<r:
                            bomb.add((j-1,k))
                        if 0<=j+1<r:
                            bomb.add((j+1,k))
                        if 0<=k-1<c:
                            bomb.add((j,k-1))
                        if 0<=k+1<c:
                            bomb.add((j,k+1))
        else:
            for j in range(r):
                for k in range(c):
                    if (j,k) in bomb:
                        arr[j][k]='.'
                    else:
                        arr[j][k]='O'
    for i in range(r):
        print(''.join(arr[i]))