def solution(quiz):
    answer = []
    for i in quiz:
        divide=i.split(" ")
        if divide[1]=="+":
            if int(divide[0])+int(divide[2])==int(divide[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(divide[0])-int(divide[2])==int(divide[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer