def solution(data, ext, val_ext, sort_by):
    answer = []
    standard=0
    standardsort=0
    if ext=='date':
        standard=1
    elif ext=='maximum':
        standard=2
    elif ext=='remain':
        standard=3
    if sort_by=='date':
        standardsort=1
    elif sort_by=='maximum':
        standardsort=2
    elif sort_by=='remain':
        standardsort=3
    for i in data:
        if i[standard]<val_ext:
            answer.append(i)
    answer=sorted(answer, key=lambda x: x[standardsort])
    return answer