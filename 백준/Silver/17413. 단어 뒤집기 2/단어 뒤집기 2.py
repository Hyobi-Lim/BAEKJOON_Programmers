import sys
arr=list(sys.stdin.readline().strip())
answer=[]
check=[]
for i in arr:
    if len(check)==0:
        if i==' ':
            answer.append(' ')
            continue
        else:
            check.append(i)
    else:
        if check[0]=='<':
            check.append(i)
            if i=='>':
                answer+=check
                check=[]
        else:
            if i==' ':
                answer+=check[::-1]
                answer.append(' ')
                check=[]
            elif i=='<':
                answer+=check[::-1]
                check=['<']
            else:
                check.append(i)
if len(check)!=0:
    answer+=check[::-1]
print(''.join(answer))