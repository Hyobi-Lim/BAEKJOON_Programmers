def solution(n):
    answer = ''
    while n>0:
        answer+=str(n%3)
        n//=3
    list(answer).sort(reverse=True)
    return int(answer,3)