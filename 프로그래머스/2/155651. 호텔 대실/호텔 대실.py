def solution(book_time):
    answer = 0
    allmin=[0]*(60*24)
    for i in book_time:
        start=int(i[0][0:2])*60+int(i[0][3:5])
        end=int(i[1][0:2])*60+int(i[1][3:5])
        for j in range(start,end+10):
            if j>=len(allmin):
                break
            allmin[j]+=1
    answer=max(allmin)
    return answer