import sys
n=int(sys.stdin.readline())
arr=list(sys.stdin.readline().strip())
alp_num=dict()
for i in range(n):
    alp_num[chr(ord('A')+i)]=int(sys.stdin.readline())
answer=[]
for i in range(len(arr)):
    if arr[i] in alp_num:
        arr[i]=alp_num[arr[i]]
for i in range(len(arr)):
    if arr[i]=='+':
        num1=answer.pop()
        num2=answer.pop()
        answer.append(num1+num2)
    elif arr[i]=='-':
        num1=answer.pop()
        num2=answer.pop()
        answer.append(num2-num1)
    elif arr[i]=='*':
        num1=answer.pop()
        num2=answer.pop()
        answer.append(num1*num2)
    elif arr[i]=='/':
        num1=answer.pop()
        num2=answer.pop()
        answer.append(num2/num1)
    else:
        answer.append(arr[i])
print("%.2f"%answer[0])