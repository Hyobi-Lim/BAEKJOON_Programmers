def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        now=list(skill[:])
        for j in i:
            if j==now[0]:
                now=now[1:]
            if j in now:
                now=now[1:]
                break
            if len(now)==0 or j==i[len(i)-1]:
                answer+=1
                break
    return answer