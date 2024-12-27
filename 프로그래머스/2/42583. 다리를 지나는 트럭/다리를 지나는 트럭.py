def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge=[]
    on_bridge_time=[]
    while(answer==0 or len(on_bridge)!=0):
        answer+=1
        if len(on_bridge_time)>=1 and answer-on_bridge_time[0]==bridge_length:
            on_bridge=on_bridge[1:]
            on_bridge_time=on_bridge_time[1:]
        if len(truck_weights)>=1 and sum(on_bridge)+truck_weights[0]<=weight:
            on_bridge.append(truck_weights[0])
            truck_weights=truck_weights[1:]
            on_bridge_time.append(answer)
    return answer