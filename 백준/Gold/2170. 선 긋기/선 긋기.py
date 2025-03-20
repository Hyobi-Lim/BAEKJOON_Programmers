import sys
n=int(sys.stdin.readline())
numset=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    numset.append([x,y])
numset=sorted(numset,key=lambda x:(x[0],x[1]))
final=[numset[0]]
for i in range(1,n):
    if final[len(final)-1][1]<numset[i][0]:
        final.append(numset[i])
    else:
        final[len(final)-1][1]=max(final[len(final)-1][1],numset[i][1])
answer=0
for i in final:
    answer+=(i[1]-i[0])
print(answer)