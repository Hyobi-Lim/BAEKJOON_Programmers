def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)-1,-1,-1):
        if B[i]>A[i]:
            answer+=1
            del A[i]
            del B[i]
        else:
            del A[i]
            del B[0]
    return answer