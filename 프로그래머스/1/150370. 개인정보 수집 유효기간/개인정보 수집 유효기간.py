import re
def solution(today, terms, privacies):
    answer = []
    today=today.split('.')
    today=list(map(int,today))
    days={}
    for i in range(len(terms)):
        terms[i]=terms[i].split()
        days[terms[i][0]]=terms[i][1]
    terms=days
    for i in range(len(privacies)):
        privacies[i]=re.split('[. ]',privacies[i])
        privacies[i][2]=int(privacies[i][2])
        privacies[i][1]=int(privacies[i][1])+int(days[privacies[i][3]])
        if privacies[i][1]%12!=0:
            privacies[i][0]=int(privacies[i][0])+privacies[i][1]//12
            privacies[i][1]%=12
        else:
            privacies[i][0]=int(privacies[i][0])+privacies[i][1]//12-1
            privacies[i][1]=12
        if today[0]>privacies[i][0]:
            answer.append(i+1)
        elif today[0]==privacies[i][0]:
            if today[1]>privacies[i][1]:
                answer.append(i+1)
            elif today[1]==privacies[i][1]:
                if today[2]>=privacies[i][2]:
                    answer.append(i+1)
    return answer