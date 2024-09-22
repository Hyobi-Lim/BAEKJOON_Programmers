def solution(fees, records):
    answer = []
    carinnout=dict()
    carfee=dict()
    carnum=[]
    for i in records:
        if i[6:10] not in carinnout:
            carinnout[i[6:10]]=[int(i[0:2])*60+int(i[3:5])]
        else:
            carinnout[i[6:10]].append(int(i[0:2])*60+int(i[3:5]))
        if i[6:10] not in carfee:
            carfee[i[6:10]]=0
        if i[6:10] not in carnum:
            carnum.append(i[6:10])
    for i in carinnout:
        nownum=0
        for j in range(0,len(carinnout[i]),2):
            if j==len(carinnout[i])-1 and len(carinnout[i])%2==1:
                nownum+=(1439-carinnout[i][j])
            else:
                nownum+=(carinnout[i][j+1]-carinnout[i][j])
        if nownum<=fees[0]:
            carfee[i]+=fees[1]
        elif (nownum-fees[0])%fees[2]==0:
            carfee[i]+=(fees[1]+(nownum-fees[0])//fees[2]*fees[3])
        else:
            carfee[i]+=(fees[1]+((nownum-fees[0])//fees[2]+1)*fees[3])
    carnum.sort()
    for i in carnum:
        answer.append(carfee[i])
    return answer