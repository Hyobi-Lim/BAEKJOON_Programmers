def solution(keymap, targets):
    answer = []
    touchnum={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for i in keymap:
        for j in range(len(i)):
            if touchnum[i[j]]==0 or touchnum[i[j]]>j+1:
                touchnum[i[j]]=j+1
    for i in targets:
        num=0
        for j in i:
            if touchnum[j]==0:
                num=-1
                break
            else:
                num+=touchnum[j]
        answer.append(num)
    return answer