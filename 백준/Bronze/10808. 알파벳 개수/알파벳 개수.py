S=input()
alp=dict()
for i in range(26):
    alp[i]=0
for i in range(len(S)):
    alp[ord(S[i])-ord('a')]+=1
for i in range(26):
    print(alp[i],end=' ')