from bisect import bisect_left
def solution(info, query):
    answer = []
    info_set=dict()
    def every_info(info,score,now,now_info):
        if now==4:
            if now_info not in info_set:
                info_set[now_info]=[score]
            else:
                info_set[now_info].append(score)
        else:
            every_info(info,score,now+1,now_info+info[now])
            every_info(info,score,now+1,now_info+'-')
    for i in range(len(info)):
        info[i]=info[i].split(' ')
        score=int(info[i].pop())
        every_info(info[i],score,0,'')
    for key in info_set:
        info_set[key].sort()
    for i in range(len(query)):
        now=[]
        for j in query[i].split(" and "):
            now.extend(j.split(" "))
        now_sen=''.join(now[:4])
        num=0
        score=int(now[4])
        if now_sen in info_set:
            num=len(info_set[now_sen])-bisect_left(info_set[now_sen],score)
        answer.append(num)
    return answer