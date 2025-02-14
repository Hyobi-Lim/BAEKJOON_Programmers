import sys
n=int(sys.stdin.readline())
answer=0
for i in range(n):
    string=sys.stdin.readline().strip()
    stack=[]
    for j in range(len(string)):
        if len(stack)==0:
            stack.append(string[j])
        else:
            if stack[len(stack)-1]==string[j]:
                stack.pop()
            else:
                stack.append(string[j])
    if len(stack)==0:
        answer+=1
print(answer)