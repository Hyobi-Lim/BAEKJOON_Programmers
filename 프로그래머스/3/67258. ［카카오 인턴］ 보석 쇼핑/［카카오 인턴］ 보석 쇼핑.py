def solution(gems):
    gems_types=len(set(gems))
    gems_count={}
    start=0
    answer=[0,len(gems)-1]
    if gems_types==1:
        answer=[1,1]
    elif len(gems)==gems_types:
        answer=[1,len(gems)]
    else:
        for end in range(len(gems)):
            gems_count[gems[end]]=gems_count.get(gems[end],0)+1
            while(len(gems_count)==gems_types and start<=end):
                if end-start<answer[1]-answer[0]:
                    answer=[start,end]
                gems_count[gems[start]]-=1
                if gems_count[gems[start]]==0:
                    del gems_count[gems[start]]
                start+=1
        answer[0]+=1
        answer[1]+=1
    return answer