import sys
n=int(sys.stdin.readline())
sour_bitter=[]
for i in range(n):
    sour,bitter=map(int,sys.stdin.readline().split())
    sour_bitter.append([sour,bitter])
answer=1000000000
def sour_bitter_check(index,sour,bitter):
    global answer
    if index>=len(sour_bitter):
        if sour!=0 and bitter!=0 and answer>abs(sour-bitter):
            answer=abs(sour-bitter)
        return
    else:
        if sour!=0 and bitter!=0 and answer>abs(sour-bitter):
            answer=abs(sour-bitter)
        sour_bitter_check(index+1,sour,bitter)
        if sour==0:
            sour_bitter_check(index+1,sour_bitter[index][0],bitter+sour_bitter[index][1])
        else:
            sour_bitter_check(index+1,sour*sour_bitter[index][0],bitter+sour_bitter[index][1])
sour_bitter_check(0,0,0)
print(answer)