def solution(msg):
    answer = []
    mydict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    w=0
    c=0
    last=27
    for i in range(1,len(msg)):
        c=i
        if msg[w:c+1] in mydict:
            continue
        else:
            answer.append(mydict[msg[w:c]])
            mydict[msg[w:c+1]]=last
            last+=1
            w=i
    answer.append(mydict[msg[w:]])
    return answer