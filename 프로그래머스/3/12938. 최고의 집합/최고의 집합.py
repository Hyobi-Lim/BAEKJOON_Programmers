def solution(n, s):
    answer = [s//n]*n
    for i in range(s%n):
        answer[len(answer)-1-i]+=1
    if s<n:
        answer=[-1]
    return answer