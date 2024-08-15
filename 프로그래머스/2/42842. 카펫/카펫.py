def solution(brown, yellow):
    answer = []
    plus=brown+yellow
    for i in range(1,plus//2+1):
        if plus%i==0 and (i-2)*(plus//i-2)==yellow:
            answer=[plus//i,i]
            break
    return answer