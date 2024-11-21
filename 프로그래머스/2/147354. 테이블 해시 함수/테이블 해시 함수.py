def solution(data, col, row_begin, row_end):
    answer = 0
    data=sorted(data,key=lambda x:x[0],reverse=True)
    data=sorted(data,key=lambda x:x[col-1])
    for i in range(row_begin-1,row_end):
        num=0
        for j in range(len(data[i])):
            num+=(data[i][j]%(i+1))
        if i==row_begin-1:
            answer=num
        else:
            answer=answer^num
    return answer