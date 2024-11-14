import math
def solution(n, stations, w):
    answer = 0
    for i in range(len(stations)):
        if i==0:
            answer+=math.ceil((stations[0]-w-1)/(2*w+1))
        else:
            answer+=math.ceil((stations[i]-stations[i-1]-2*w-1)/(2*w+1))
    answer+=math.ceil((n-stations[len(stations)-1]-w)/(2*w+1))
    return answer