def solution(operations):
    answer = []
    now=[]
    for i in operations:
        if i[0]=="I":
            now.append(int(i[2:]))
        else:
            if len(now)==0:
                continue
            else:
                if i[2]=="-":
                    now.remove(min(now))
                else:
                    now.remove(max(now))
    if len(now)==0:
        answer=[0,0]
    else:
        answer=[max(now),min(now)]
    return answer