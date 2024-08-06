def solution(players, callings):
    playersdict={}
    for i in range(len(players)):
        playersdict[players[i]]=i
    for i in callings:
        num=playersdict[i]
        players[num-1],players[num]=players[num],players[num-1]
        playersdict[players[num-1]]=num-1
        playersdict[players[num]]=num
    return players