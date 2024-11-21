import copy
def solution(tickets):
    def findway(now,rest):
        if len(rest)==0:
            answer.append(now)
            return
        if now[len(now)-1] not in rest:
            return
        for i in range(len(rest[now[len(now)-1]])):
            newrest=copy.deepcopy(rest)
            del newrest[now[len(now)-1]][i]
            if len(newrest[now[len(now)-1]])==0:
                del newrest[now[len(now)-1]]
            findway(now+[rest[now[len(now)-1]][i]],newrest)
    answer = []
    citydict=dict()
    for i in tickets:
        if i[0] not in citydict:
            citydict[i[0]]=[i[1]]
        else:
            citydict[i[0]].append(i[1])
    findway(['ICN'],citydict)
    answer.sort()
    answer=answer[0]
    return answer