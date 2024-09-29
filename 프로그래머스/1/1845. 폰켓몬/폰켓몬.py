def solution(nums):
    answer = 0
    numsset=set(nums)
    if len(numsset)>=len(nums)/2:
        answer=len(nums)/2
    else:
        answer=len(numsset)
    return answer