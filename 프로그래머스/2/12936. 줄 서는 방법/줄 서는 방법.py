def solution(n, k):
    answer = []
    all=[i for i in range(1,n+1)]
    num=1
    for i in range(1,n):
        num*=i
    k-=1
    for i in range(n-1):
        answer.append(all[k//num])
        del all[k//num]
        k%=num
        num//=(n-i-1)
    answer+=all
    return answer