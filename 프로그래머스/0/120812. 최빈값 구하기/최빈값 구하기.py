def solution(array):
    answer = 0
    norepeat=list(set(array))
    countli=[]
    for i in norepeat:
        countli.append(array.count(i))
    if countli.count(max(countli))==1:
        answer=norepeat[countli.index(max(countli))]
    else:
        answer=-1
    return answer