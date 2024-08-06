def solution(X, Y):
    answer = 0
    Xdict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    Ydict={'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for i in X:
        Xdict[i]+=1
    for i in Y:
        Ydict[i]+=1
    num=[]
    for i in range(9,-1,-1):
        num+=([str(i)]*min(Xdict[str(i)],Ydict[str(i)]))
    if len(num)==0:
        answer='-1'
    elif num[0]=='0':
        answer='0'
    else:
        answer=''.join(num)
    return answer