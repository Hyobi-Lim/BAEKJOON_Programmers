def solution(p):
    answer = ''
    def rightsentence(w):
        if len(w)==0:
            return w
        else:
            numcheck={'(':0,')':0}
            u=''
            v=''
            for i in range(len(w)):
                numcheck[w[i]]+=1
                if numcheck['(']==numcheck[')']:
                    u=w[:i+1]
                    v=w[i+1:]
                    break
            if checkright(u)==True:
                return u+rightsentence(v)
            else:
                now='('
                now+=rightsentence(v)
                now+=')'
                u=u[1:len(u)-1]
                for i in range(len(u)):
                    if u[i]=='(':
                        now+=')'
                    else:
                        now+='('
                return now
    def checkright(str):
        result=True
        stack=[]
        for i in range(len(str)):
            if str[i]=='(':
                stack.append(str[i])
            else:
                if len(stack)==0:
                    result=False
                    break
                else:
                    stack.pop()
        return result
    if checkright(p)==True:
        answer=p
    else:
        answer=rightsentence(p)
    return answer