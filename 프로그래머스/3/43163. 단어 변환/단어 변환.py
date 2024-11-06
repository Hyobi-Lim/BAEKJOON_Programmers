def solution(begin, target, words):
    answer=0
    def findword(begin,target,words,number):
        nonlocal answer
        if begin==target:
            if answer==0:
                answer=number
            elif answer>number:
                answer=number
            return
        else:
            for i in range(len(words)):
                num=0
                for j in range(len(words[i])):
                    if words[i][j]!=begin[j]:
                        num+=1
                if num==1:
                    newwords=words[:]
                    newstart=newwords[i]
                    del newwords[i]
                    findword(newstart,target,newwords,number+1)
    if target in words:
        for i in range(len(words)):
            num=0
            for j in range(len(words[i])):
                if words[i][j]!=begin[j]:
                    num+=1
            if num==1:
                newwords=words[:]
                newstart=newwords[i]
                del newwords[i]
                findword(newstart,target,newwords,1)
    return answer