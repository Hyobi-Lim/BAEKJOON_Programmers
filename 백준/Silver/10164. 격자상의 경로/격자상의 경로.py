import sys
n,m,k=map(int,sys.stdin.readline().split())
if k==0:
    first=[[0]*m for _ in range(n)]
    for i in range(len(first)):
        for j in range(len(first[i])):
            if i==0 or j==0:
                first[i][j]=1
            else:
                first[i][j]=first[i-1][j]+first[i][j-1]
    print(first[len(first)-1][len(first[0])-1])
else:
    first=[[0]*((k-1)%m+1) for _ in range((k-1)//m+1)]
    for i in range(len(first)):
        for j in range(len(first[i])):
            if i==0 or j==0:
                first[i][j]=1
            else:
                first[i][j]=first[i-1][j]+first[i][j-1]
    second=[[0]*(m-((k-1)%m+1)+1) for _ in range(n-((k-1)//m+1)+1)]
    for i in range(len(second)):
        for j in range(len(second[i])):
            if i==0 or j==0:
                second[i][j]=1
            else:
                second[i][j]=second[i-1][j]+second[i][j-1]
    print(first[len(first)-1][len(first[0])-1]*second[len(second)-1][len(second[0])-1])