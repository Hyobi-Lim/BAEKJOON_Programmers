def solution(babbling):
    answer = 0
    for i in range(len(babbling)):
        num=''
        while(babbling[i][:3]=="aya" or babbling[i][:3]=="woo" or babbling[i][:2]=="ye" or babbling[i][:2]=="ma"):
            if babbling[i][:3]=="aya":
                num+='1'
                babbling[i]=babbling[i][3:]
            elif babbling[i][:3]=="woo":
                num+='2'
                babbling[i]=babbling[i][3:]
            elif babbling[i][:2]=="ye":
                num+='3'
                babbling[i]=babbling[i][2:]
            elif babbling[i][:2]=="ma":
                num+='4'
                babbling[i]=babbling[i][2:]
        if babbling[i]=='' and '11' not in num and '22' not in num and '33' not in num and '44' not in num:
            answer+=1
    return answer