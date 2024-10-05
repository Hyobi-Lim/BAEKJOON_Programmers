def solution(babbling):
    answer = 0
    canspeak=["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        while(True):
            if len(babbling[i])<2:
                break
            elif babbling[i][0:3]=="aya" or babbling[i][0:3]=="woo":
                babbling[i]=babbling[i][3:]
                continue
            elif babbling[i][0:2]=="ye" or babbling[i][0:2]=="ma":
                babbling[i]=babbling[i][2:]
                continue
            else:
                break
    for i in babbling:
        if i=="":
            answer+=1
    return answer