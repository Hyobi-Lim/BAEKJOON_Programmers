def solution(citations):
    answer = 0
    for i in range(max(citations)+1):
        num=0
        for j in citations:
            if j>=i:
                num+=1
        if num>=i and num>answer:
            answer=i
    return answer