def solution(lottos, win_nums):
    answer = []
    same=0
    zero=lottos.count(0)
    for i in lottos:
        if i in win_nums:
            same+=1
    if 6-same-zero+1>=6:
        answer.append(6)
    else:
        answer.append(6-same-zero+1)
    if 6-same+1>=6:
        answer.append(6)
    else:
        answer.append(6-same+1)
    return answer