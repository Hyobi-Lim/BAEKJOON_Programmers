def solution(s):
    answer = True
    s=list(s)
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z':
                answer=False  
    else:
        answer=False         
    return answer