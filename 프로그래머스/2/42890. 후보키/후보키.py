def solution(relation):
    answer = 0
    everykey=[]
    def checkall(relation,include,now):
        if now==len(relation[0]):
            if include==[]:
                return
            else:
                new=set()
                for i in range(len(relation)):
                    rn=[]
                    for j in include:
                        rn.append(relation[i][j])
                    new.add(tuple(rn))
                if len(new)==len(relation):
                    everykey.append(set(include))
        else:
            checkall(relation,include+[now],now+1)
            checkall(relation,include,now+1)
    checkall(relation,[],0)
    fewkey=[]
    for i in everykey:
        for j in everykey:
            if i!=j and i==i.intersection(j):
                fewkey.append(j)
    for i in everykey:
        if i not in fewkey:
            answer+=1
    return answer