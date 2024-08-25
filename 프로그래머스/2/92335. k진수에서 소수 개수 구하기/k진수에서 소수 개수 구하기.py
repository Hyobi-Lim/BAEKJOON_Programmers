def divide(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
def solution(n, k):
    answer = 0
    num=str(divide(n, k)).split('0')
    for i in num:
        if i=='':
            continue
        now=int(i)
        if now==1:
            continue
        prime=0
        for j in range(2,int(now**0.5)+1):
            if now%j==0:
                prime+=1
                break
        if prime==0:
            answer+=1
    return answer