def solution(s, n):
    answer = ''
    for i in s:
        if 'a'<=i<='z':
            answer+=chr(ord('a')+(ord(i)-ord('a')+n)%26)
        elif i==' ':
            answer+=' '
        else:
            answer+=chr(ord('A')+(ord(i)-ord('A')+n)%26)
    return answer