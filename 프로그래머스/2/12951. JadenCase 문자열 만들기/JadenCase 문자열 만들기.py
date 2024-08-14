def solution(s):
    s=s.lower()
    ran=['0','1','2','3','4','5','6','7','8','9',' ']
    for i in range(len(s)):
        if i==0 and s[0] not in ran:
            s=s[0].upper()+s[1:]
        elif s[i]==' ' and i!=len(s)-1 and s[i+1] not in ran:
            s=s[:i+1]+s[i+1].upper()+s[i+2:]
    return s