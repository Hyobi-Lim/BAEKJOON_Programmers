def solution(sizes):
    answer = 0
    num1=[]
    num2=[]
    for i in sizes:
        if i[0]>i[1]:
            i[0],i[1]=i[1],i[0]
        num1.append(i[0])
        num2.append(i[1])
    answer=max(num1)*max(num2)
    return answer