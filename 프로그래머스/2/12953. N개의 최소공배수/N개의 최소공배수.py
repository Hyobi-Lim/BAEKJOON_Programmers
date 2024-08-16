def solution(arr):
    answer = arr[0]
    arr.sort()
    for i in arr:
        num=answer
        while(answer%i!=0):
            answer+=num
    return answer