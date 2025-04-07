import sys
arr=list(sys.stdin.readline().replace('()','#'))
parentheses_set=0
answer=0
stack=[]
for i in range(len(arr)):
    if arr[i]=='#':
        answer+=(len(stack)+parentheses_set)
        parentheses_set=0
    elif arr[i]=='(':
        stack.append(arr[i])
    elif arr[i]==')':
        stack.pop()
        parentheses_set+=1
answer+=(len(stack)+parentheses_set)
print(answer)