def solution(numbers, target):
    answer = 0
    all=[0]
    for i in range(len(numbers)):
        new=[]
        for j in range(2**i-1,-1,-1):
            new.append(all[len(all)-j-1]+numbers[i])
            new.append(all[len(all)-j-1]-numbers[i])
        all+=new
    all=all[len(all)-2**len(numbers):]
    for i in all:
        if i==target:
            answer+=1
    return answer