def solution(priorities, location):
    queue=[]
    for i in range(len(priorities)):
        queue.append(chr(0+i))
    play=[]
    while(chr(0+location) not in play):
        if priorities[0]>=max(priorities):
            play.append(queue[0])
            priorities=priorities[1:]
            queue=queue[1:]
        else:
            priorities=priorities[1:]+[priorities[0]]
            queue=queue[1:]+[queue[0]]
    answer=len(play)
    return answer