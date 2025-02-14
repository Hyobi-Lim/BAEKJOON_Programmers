s=input()
s=s.upper()
alp=dict()
for i in range(len(s)):
    if s[i] in alp:
        alp[s[i]]+=1
    else:
        alp[s[i]]=1
aplvalue=list(alp.values())
aplvalue.sort(reverse=True)
answer='?'
if len(aplvalue)==1 or aplvalue[0]!=aplvalue[1]:
    for i in alp:
        if alp[i]==aplvalue[0]:
            answer=i
            break
print(answer)