def solution(storey):
    answer = 0
    while(storey>0):
        if storey%10>5:
            answer+=(10-storey%10)
            storey//=10
            storey+=1
        elif storey%10==5:
            if storey//10%10>=5:
                answer+=(10-storey%10)
                storey//=10
                storey+=1
            else:
                answer+=(storey%10)
                storey//=10
        else:
            answer+=(storey%10)
            storey//=10
    return answer