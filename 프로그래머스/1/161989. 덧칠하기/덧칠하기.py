def solution(n, m, section):
    answer = 0
    now=set([])
    for i in section:
        if i in now:
            continue
        else:
            for i in range(i,i+m):
                now.add(i)
            answer+=1
    return answer