def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        num=0
        for j in photo[i]:
            if j in name:
                num+=yearning[name.index(j)]
        answer.append(num)
    return answer