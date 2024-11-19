def solution(orders, course):
    def pickcourse(idx, sidx, arr, sel):
        if sidx == len(sel):
            now=''.join(sel)
            if len(now) not in allcourse:
                allcourse[len(now)]=dict()
                allcourse[len(now)][now]=1
            else:
                if now in allcourse[len(now)]:
                    allcourse[len(now)][now]+=1
                else:
                    allcourse[len(now)][now]=1
            return
        if idx == len(arr):
            return
        sel[sidx] = arr[idx]
        pickcourse(idx+1, sidx+1, arr, sel)
        pickcourse(idx+1, sidx, arr, sel)
    answer = []
    allcourse=dict()
    for i in range(len(orders)):
        orders[i]=list(orders[i])
        orders[i].sort()
        for j in range(len(course)):
            if len(orders[i])>=course[j]:
                pickcourse(0, 0, orders[i], [0]*course[j])
    for i in allcourse:
        allcourse[i] = dict(sorted(allcourse[i].items(), key=lambda item: item[1], reverse=True))
        count=0
        num=0
        for j in allcourse[i]:
            if count==0:
                count+=1
                num=allcourse[i][j]
            if allcourse[i][j]==num and allcourse[i][j]>=2:
                answer.append(j)
    answer = sorted(answer)
    return answer