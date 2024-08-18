def solution(clothes):
    answer = 1
    clothesdict={}
    for i in clothes:
        if i[1] not in clothesdict:
            clothesdict[i[1]]=1
        else:
            clothesdict[i[1]]+=1
    for i in clothesdict:
        print(i)
        answer*=clothesdict[i]+1
    answer-=1
    return answer