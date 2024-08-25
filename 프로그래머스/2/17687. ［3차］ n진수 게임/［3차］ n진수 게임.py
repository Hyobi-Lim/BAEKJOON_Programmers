def divide(n, q):
    rev_base = ''
    while n>0:
        n,mod=divmod(n, q)
        if mod<=9:
            rev_base+=str(mod)
        else:
            rev_base+=chr(ord('A')+mod-10)
    return rev_base[::-1] 
def solution(n, t, m, p):
    answer = ''
    fullanswer=''
    num=0
    while(len(fullanswer)<(t-1)*m+p):
        if num==0:
            fullanswer+='0'
        else:
            fullanswer+=str(divide(num,n))
        num+=1
    for i in range(p-1,len(fullanswer),m):
        answer+=fullanswer[i]
        if len(answer)==t:
            break
    return answer