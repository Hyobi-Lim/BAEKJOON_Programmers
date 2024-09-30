def solution(files):
    answer = []
    number=['0','1','2','3','4','5','6','7','8','9']
    headnum=dict()
    for i in range(len(files)):
        now=['','','',0,'']
        numcheck=False
        for j in range(len(files[i])):
            if numcheck==False and files[i][j] in number:
                numcheck=True
                now[2]+=files[i][j]
            elif numcheck==True and files[i][j] in number:
                now[2]+=files[i][j]
            elif numcheck==True and files[i][j] not in number:
                now[3]=int(now[2])
                now[4]=files[i][j:]
                if now[1] not in headnum:
                    headnum[now[1]]=1
                else:
                    headnum[now[1]]+=1
                answer.append(now)
                break
            else:
                now[0]+=files[i][j]
                if 'A'<=files[i][j]<='Z':
                    now[1]+=files[i][j].lower()
                else:
                    now[1]+=files[i][j]
            if j==len(files[i])-1:
                now[3]=int(now[2])
                if now[1] not in headnum:
                    headnum[now[1]]=1
                else:
                    headnum[now[1]]+=1
                answer.append(now)
    answer = sorted(answer, key=lambda x: x[1])
    for i in range(len(answer)):
        if headnum[answer[i][1]]>=2:
            headnum1=sorted(answer[i:i+headnum[answer[i][1]]], key=lambda x: x[3])
            answer=answer[:i]+headnum1+answer[i+headnum[answer[i][1]]:]
            headnum[answer[i][1]]=1
    for i in range(len(answer)):
        answer[i]=answer[i][0]+answer[i][2]+answer[i][4]
    return answer