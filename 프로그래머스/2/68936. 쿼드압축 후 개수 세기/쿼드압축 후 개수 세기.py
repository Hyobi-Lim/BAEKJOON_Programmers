def solution(arr):
    def quadcheck(quadqrr,quadnum):
        if num==1:
            for i in range(2):
                for j in range(2):
                    if quadqrr[i][j]==0:
                        answer[0]+=1
                    else:
                        answer[1]+=1
            return
        else:
            for i in range(4):
                now=[]
                for a in range(quadnum):
                    if i==0:
                        now.append(quadqrr[0+a][:quadnum])
                    elif i==1:
                        now.append(quadqrr[0+a][quadnum:])
                    elif i==2:
                        now.append(quadqrr[quadnum+a][:quadnum])
                    else:
                        now.append(quadqrr[quadnum+a][quadnum:])
                if now==[[0]*quadnum]*quadnum:
                    answer[0]+=1
                elif now==[[1]*quadnum]*quadnum:
                    answer[1]+=1
                else:
                    quadcheck(now,quadnum//2)
    answer = [0,0]
    num=len(arr)
    if arr==[[0]*num]*num:
        answer[0]+=1
    elif arr==[[1]*num]*num:
        answer[1]+=1
    else:
        quadcheck(arr,num//2)
    return answer