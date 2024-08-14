def solution(s):
    answer = ''
    s=s.split()
    for i in range(len(s)):
        s[i]=int(s[i])
    answer+=str(min(s))
    answer+=' '
    answer+=str(max(s))
    return answer