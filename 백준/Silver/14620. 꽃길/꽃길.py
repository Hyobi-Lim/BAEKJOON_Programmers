import sys
n=int(sys.stdin.readline())
arr=[list(map(int,input().split())) for _ in range(n)]
answer=3000
index=[]
for i in range(1,n-1):
    for j in range(1,n-1):
        index.append([i,j])
for i in range(len(index)-2):
    for j in range(i+1,len(index)-1):
        for k in range(j+1,len(index)):
            a1,a2=index[i]
            b1,b2=index[j]
            c1,c2=index[k]
            now=set([(a1,a2),(a1-1,a2),(a1,a2-1),(a1+1,a2),(a1,a2+1),
                    (b1,b2),(b1-1,b2),(b1,b2-1),(b1+1,b2),(b1,b2+1),
                    (c1,c2),(c1-1,c2),(c1,c2-1),(c1+1,c2),(c1,c2+1)])
            if len(now)!=15:
                continue
            price=0
            for l in now:
                price+=arr[l[0]][l[1]]
            if answer>price:
                answer=price
print(answer)