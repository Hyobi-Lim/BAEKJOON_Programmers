def solution(scores):
    answer = 1
    original=scores[0]
    sumoriginal=scores[0][0]+scores[0][1]
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxone=scores[0][1]
    for i in range(len(scores)):
        if original[0]<scores[i][0] and original[1]<scores[i][1]:
            answer=-1
            break
        if scores[i][1]<maxone:
            continue
        elif scores[i][1]>maxone:
            maxone=scores[i][1]
        if scores[i][0]+scores[i][1]>sumoriginal:
            answer+=1
    return answer