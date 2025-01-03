def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        if numbers[i]%2==0:
            answer.append(numbers[i]+1)
        else:
            binum=format(numbers[i],'b')
            if binum=='1'*len(binum):
                binum='10'+'1'*(len(binum)-1)
            else:
                for j in range(len(binum)-1,-1,-1):
                    if binum[j]=='0':
                        if j==len(binum)-1:
                            binum=binum[:j]+'1'
                        else:
                            binum=binum[:j]+'10'+binum[j+2:]
                        break
            answer.append(int(binum,2))
    return answer