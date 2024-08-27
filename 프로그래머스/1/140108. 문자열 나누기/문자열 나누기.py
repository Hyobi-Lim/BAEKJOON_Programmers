def solution(s):
    answer = 0
    first=s[0]
    xnum=0
    notxnum=0
    for i in range(len(s)):
        if first==s[i]:
            xnum+=1
        else:
            notxnum+=1
        if xnum==notxnum:
            answer+=1
            xnum=0
            notxnum=0
            if i!=len(s)-1:
                first=s[i+1]
        else:
            if i==len(s)-1:
                answer+=1
                break
    return answer