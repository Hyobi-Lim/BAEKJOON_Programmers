def solution(s):
    answer = []
    now=[]
    for i in s:
        if i not in now:
            answer.append(-1)
        else:
            for j in range(len(now)-1,-1,-1):
                if i==now[j]:
                    answer.append(len(now)-j)
                    break
        now.append(i)
    return answer