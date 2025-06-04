import sys
n=int(sys.stdin.readline())
tower=list(map(int,sys.stdin.readline().split()))
stack=[[tower[0],1]]
answer=[0]
for i in range(1,n):
    while(stack):
        height,index=stack.pop()
        if height>=tower[i]:
            answer.append(index)
            stack.append([height,index])
            break
    if len(stack)==0:
        answer.append(0)
    stack.append([tower[i],i+1])
print(*answer)