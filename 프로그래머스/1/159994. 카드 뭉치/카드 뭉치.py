def solution(cards1, cards2, goal):
    answer = 'Yes'
    num1=0
    num2=0
    for i in range(len(goal)):
        if num1<len(cards1) and goal[i]==cards1[num1]:
            num1+=1
            continue
        elif num2<len(cards2) and goal[i]==cards2[num2]:
            num2+=1
            continue
        else:
            answer='No'
            break
    return answer