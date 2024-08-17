def solution(s):
    answer = 0
    for i in range(len(s)):
        news=s[i:]+s[:i]
        while('()' in news or '[]' in news or '{}' in news):
            news=news.replace('()','')
            news=news.replace('[]','')
            news=news.replace('{}','')
        if len(news)==0:
            answer+=1
    return answer