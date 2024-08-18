def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        new=[]
        for j in range(len(arr2[0])):
            num=0
            for k in range(len(arr2)):
                num+=arr1[i][k]*arr2[k][j]
            new.append(num)
        answer.append(new)
    return answer