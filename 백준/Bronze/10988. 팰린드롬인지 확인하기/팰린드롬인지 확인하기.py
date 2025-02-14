s=input()
answer=1
for i in range(len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        answer=0
        break
print(answer)