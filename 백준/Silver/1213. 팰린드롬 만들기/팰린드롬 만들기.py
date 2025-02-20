import sys
n=sys.stdin.readline().strip()
alp=dict()
oddnum=0
for i in range(len(n)):
    if n[i] in alp:
        alp[n[i]]+=1
    else:
        alp[n[i]]=1
for i in alp:
    if alp[i]%2==1:
        oddnum+=1
answer="I'm Sorry Hansoo"
if len(n)%2==0 and oddnum==0:
    answer=[]
    for i in alp:
        answer+=(alp[i]//2*[i])
    answer.sort()
    rev=answer[:]
    rev.reverse()
    answer+=rev
elif len(n)%2==1 and oddnum==1:
    answer=[]
    odd_alp=''
    for i in alp:
        if alp[i]%2==1:
            odd_alp=i
        answer+=(alp[i]//2*[i])
    answer.sort()
    answer.append(odd_alp)
    rev=answer[:]
    rev.pop()
    rev.reverse()
    answer+=rev
print(''.join(answer))