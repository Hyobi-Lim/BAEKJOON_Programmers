import sys
n=int(sys.stdin.readline())
for i in range(n):
    answer="YES"
    str=sys.stdin.readline().strip()
    stack=[]
    for j in range(len(str)):
        if str[j]=='(':
            stack.append(str[j])
        else:
            if len(stack)==0:
                answer="NO"
                break
            else:
                stack.pop()
    if len(stack)!=0:
        answer="NO"
    print(answer)