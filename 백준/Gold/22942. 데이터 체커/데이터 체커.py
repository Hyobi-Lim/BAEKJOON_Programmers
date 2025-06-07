import sys
n=int(sys.stdin.readline())
circles=[]
for i in range(n):
    x,r=map(int,sys.stdin.readline().split())
    circles.append((x-r,x+r))
circles.sort()
stack=[]
answer='YES'
for i in circles:
    if len(stack)==0:
        stack.append(i)
    elif len(stack)==1:
        if stack[0][1]<i[0]:
            stack=[i]
        elif (stack[0][0]<i[0]<stack[0][1] and stack[0][0]<i[1]<stack[0][1]) or (stack[0][0]<i[0]<stack[0][1] and stack[0][0]<i[1]<stack[0][1]):
            stack.append(i)
        else:
            answer='NO'
            break
    else:
        for j in stack:
            if j[1]<i[0] or (i[0]<j[0]<i[1] and i[0]<j[1]<i[1]) or (j[0]<i[0]<j[1] and j[0]<i[1]<j[1]):
                continue
            else:
                answer='NO'
                break
        if answer=='NO':
            break
print(answer)