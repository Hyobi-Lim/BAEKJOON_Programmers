def solution(k, m, score):
    answer = 0
    score.sort()
    num=len(score)-m
    while num>=0:
        answer+=(score[num]*m)
        num-=m
    return answer