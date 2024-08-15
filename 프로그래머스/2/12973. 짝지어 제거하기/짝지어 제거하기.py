def solution(s):
    answer = 0
    now=[]
    for i in range(len(s)):
        if i==0 or len(now)==0:
            now.append(s[i])
        elif now[len(now)-1]==s[i]:
            now.pop()
        else:
            now.append(s[i])
    if len(now)==0:
        answer+=1
    return answer