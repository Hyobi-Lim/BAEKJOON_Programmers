import sys
from itertools import combinations
str=list(sys.stdin.readline().strip())
parentheses=[]
stack=[]
for i in range(len(str)):
    if str[i]=='(':
        stack.append(i)
    elif str[i]==')':
        parentheses.append([stack.pop(),i])
answer=set()
for i in range(1,len(parentheses)+1):
    for j in list(combinations(parentheses,i)):
        now=[]
        for k in j:
            now+=list(k)
        now.sort(reverse=True)
        formula=str[:]
        for k in now:
            del formula[k]
        answer.add(''.join(formula))
answer=list(answer)
answer.sort()
for i in answer:
    print(i)