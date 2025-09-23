def solution(sticker):
    if len(sticker)<=2:
        return max(sticker)
    answer = 0
    first_include=[0]*(len(sticker)-1)
    first_not_include=[0]*len(sticker)
    first_include[0]=sticker[0]
    first_include[1]=max(sticker[0],sticker[1])
    for i in range(2,len(first_include)):
        first_include[i]=max(first_include[i-2]+sticker[i],first_include[i-1])
    first_not_include[1]=sticker[1]
    for i in range(2,len(first_not_include)):
        first_not_include[i]=max(first_not_include[i-2]+sticker[i],first_not_include[i-1])
    answer=max(first_include[-1],first_not_include[-1])
    return answer