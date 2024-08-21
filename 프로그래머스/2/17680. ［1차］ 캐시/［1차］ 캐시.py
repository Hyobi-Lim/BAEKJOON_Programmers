def solution(cacheSize, cities):
    answer = 0
    now=[]
    if cacheSize==0:
        answer=len(cities)*5
    else:
        for i in range(len(cities)):
            cities[i]=cities[i].lower()
            if len(now)<cacheSize:
                if cities[i] in now:
                    answer+=1
                    num=now.index(cities[i])
                    now=now[:num]+now[num+1:]
                    now.append(cities[i])
                else:
                    answer+=5
                    now.append(cities[i])
            else:
                if cities[i] in now:
                    answer+=1
                    num=now.index(cities[i])
                    now=now[:num]+now[num+1:]
                    now.append(cities[i])
                else:
                    answer+=5
                    now=now[1:]
                    now.append(cities[i])
    return answer