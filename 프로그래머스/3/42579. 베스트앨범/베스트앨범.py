def solution(genres, plays):
    answer = []
    genreallnum=dict()
    genrecount=dict()
    for i in range(len(genres)):
        if genres[i] not in genreallnum:
            genreallnum[genres[i]]=plays[i]
        else:
            genreallnum[genres[i]]+=plays[i]
        if genres[i] not in genrecount:
            genrecount[genres[i]]=dict()
            genrecount[genres[i]][plays[i]]=[i]
        else:
            if plays[i] in genrecount[genres[i]]:
                genrecount[genres[i]][plays[i]].append(i)
            else:
                genrecount[genres[i]][plays[i]]=[i]
    genreallnum = dict(sorted(genreallnum.items(), key=lambda item: item[1], reverse=True))
    for i in genrecount:
        genrecount[i] = dict(sorted(genrecount[i].items(), reverse=True))
        now=[]
        for j in genrecount[i]:
            now+=genrecount[i][j]
        genrecount[i]=now
    num=0
    for i in genreallnum:
        if len(genrecount[i])<2:
            answer+=genrecount[i]
        else:
            answer+=genrecount[i][:2]
    return answer