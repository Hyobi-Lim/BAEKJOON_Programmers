def solution(nums):
    answer = 0
    sumset=[]
    for a in range(len(nums)-2):
        for b in range(a+1,len(nums)-1):
            for c in range(b+1,len(nums)):
                sumset.append(nums[a]+nums[b]+nums[c])
    for i in sumset:
        num=0
        for j in range(1,i+1):
            if i%j==0:
                num+=1
        if num==2:
            answer+=1
    return answer