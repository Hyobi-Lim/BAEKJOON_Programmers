def solution(s):
    answer = 1
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            now=s[i:j+1]
            if now==now[::-1] and len(now)>answer:
                answer=len(now)
    return answer