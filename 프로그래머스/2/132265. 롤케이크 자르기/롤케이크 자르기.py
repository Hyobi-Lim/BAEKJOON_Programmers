def solution(topping):
    answer = 0
    ob=dict()
    yb=dict()
    for i in range(len(topping)):
        if topping[i] not in ob:
            ob[topping[i]]=1
        else:
            ob[topping[i]]+=1
    for i in range(len(topping)-1,0,-1):
        if topping[i] in yb:
            yb[topping[i]]+=1
        else:
            yb[topping[i]]=1
        ob[topping[i]]-=1
        if ob[topping[i]]==0:
            del ob[topping[i]]
        if len(ob)==len(yb):
            answer+=1
    return answer