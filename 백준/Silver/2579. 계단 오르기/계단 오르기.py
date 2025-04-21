import sys
n=int(sys.stdin.readline())
stairs=[]
for i in range(n):
    stairs.append(int(sys.stdin.readline()))
answer=[[0,0] for _ in range(n)]
answer[0]=[stairs[0],stairs[0]]
for i in range(1,n):
    if n==1:
        answer[i][0]=stairs[i]
        answer[i][1]=stairs[0]+1
    else:
        answer[i][0]=max(answer[i-2])+stairs[i]
        answer[i][1]=answer[i-1][0]+stairs[i]
print(max(answer[len(answer)-1]))