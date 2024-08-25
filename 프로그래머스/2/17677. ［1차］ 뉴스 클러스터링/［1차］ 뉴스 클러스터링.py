def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    sen1=[]
    sen2=[]
    for i in range(len(str1)-1):
        if 'a'<=str1[i]<='z' and 'a'<=str1[i+1]<='z':
            sen1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if 'a'<=str2[i]<='z' and 'a'<=str2[i+1]<='z':
            sen2.append(str2[i:i+2])
    all=set(sen1)|set(sen2)
    num1=0
    num2=0
    for i in all:
        num1+=min(sen1.count(i),sen2.count(i))
        num2+=max(sen1.count(i),sen2.count(i))
    if num1==0 and num2==0:
        answer=65536
    else:
        answer=int(num1/num2*65536)
    return answer