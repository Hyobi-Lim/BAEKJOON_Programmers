import copy
def solution(user_id, banned_id):
    answer = []
    def casecheck(now,rest_banned_id,rest_banned_id_dict):
        if len(rest_banned_id)==0:
            answer.append(now)
            return
        else:
            now_banned_id=rest_banned_id[0]
            rest_banned_id=rest_banned_id[1:]
            if now_banned_id in rest_banned_id_dict:
                for i in range(len(rest_banned_id_dict[now_banned_id])):
                    now_add=rest_banned_id_dict[now_banned_id][i]
                    new_rest_banned_id_dict=copy.deepcopy(rest_banned_id_dict)
                    del new_rest_banned_id_dict[now_banned_id][i]
                    if len(new_rest_banned_id_dict[now_banned_id])==0:
                        del new_rest_banned_id_dict[now_banned_id]
                    casecheck(now+[now_add],rest_banned_id,new_rest_banned_id_dict)
            else:
                return
    banned_id_dict=dict()
    for i in range(len(banned_id)):
        nowlen=len(banned_id[i])
        banned_id_dict[banned_id[i]]=[]
        for j in range(len(user_id)):
            if len(user_id[j])==nowlen:
                for k in range(nowlen):
                    if banned_id[i][k]=='*' or banned_id[i][k]==user_id[j][k]:
                        if k==nowlen-1:
                            banned_id_dict[banned_id[i]].append(user_id[j])
                        else:
                            continue
                    else:
                        break
    casecheck([],banned_id,banned_id_dict)
    for i in range(len(answer)-1,-1,-1):
        if len(answer[i])!=len(set(answer[i])):
            del answer[i]
    answer=set(tuple(sorted(i)) for i in answer)
    answer=[list(i) for i in answer]
    answer=len(answer)
    return answer