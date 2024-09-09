def solution(n, works):
    answer = 0
    if sum(works)>n:
        while(n>0):
            works.sort(reverse=True)
            if n>=works.count(max(works)):
                for i in range(works.count(max(works))):
                    works[i]-=1
                    n-=1
            else:
                for i in range(n):
                    works[i]-=1
                    n-=1
        for i in works:
            answer+=i**2
    return answer