def solution(id_list, report, k):
    answer = []
    count={}
    reportid={}
    arrest=[]
    for i in id_list:
        count[i]=0
        reportid[i]=[]
    report=set(report)
    for i in report:
        now=list(i.split())
        count[now[1]]+=1
        reportid[now[0]].append(now[1])
    for i in id_list:
        if count[i]>=k:
            arrest.append(i)
    for i in id_list:
        num=0
        for j in reportid[i]:
            if j in arrest:
                num+=1
        answer.append(num)
    return answer