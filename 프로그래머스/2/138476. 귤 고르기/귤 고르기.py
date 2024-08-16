def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    tangerinenum=[]
    for i in range(len(tangerine)):
        if i==0 or tangerine[i]!=tangerine[i-1]:
            tangerinenum.append(i)
    tangerinenum.append(len(tangerine))
    tangerinecount=[]
    for i in range(1,len(tangerinenum)):
        tangerinecount.append(tangerinenum[i]-tangerinenum[i-1])
    tangerinecount.sort(reverse=True)
    total=0
    for i in tangerinecount:
        if total>=k:
            break
        else:
            answer+=1
            total+=i
    return answer