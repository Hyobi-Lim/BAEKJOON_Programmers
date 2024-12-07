def solution(n, m):
    answer = []
    small=1
    for i in range(min(n,m)):
        if n%(i+1)==0 and m%(i+1)==0:
            small=(i+1)
    answer.append(small)
    answer.append(small*(n//small)*(m//small))
    return answer