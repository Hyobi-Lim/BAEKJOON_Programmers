def solution(sequence):
    pm=sequence[:]
    mp=sequence[:]
    answer=pm[0]
    for i in range(len(sequence)):
        if i%2==1:
            pm[i]*=-1
        else:
            mp[i]*=-1
    nowpm=pm[0]
    for i in range(len(sequence)):
        if i!=0:
            if pm[i]>pm[i]+nowpm:
                nowpm=pm[i]
            else:
                nowpm+=pm[i]
        if nowpm>answer:
            answer=nowpm
    nowmp=mp[0]
    for i in range(len(sequence)):
        if i!=0:
            if mp[i]>mp[i]+nowmp:
                nowmp=mp[i]
            else:
                nowmp+=mp[i]
        if nowmp>answer:
            answer=nowmp
    return answer