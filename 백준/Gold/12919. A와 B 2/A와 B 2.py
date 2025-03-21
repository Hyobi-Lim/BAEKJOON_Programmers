import sys
sys.setrecursionlimit(10**6)
s=sys.stdin.readline().strip()
t=sys.stdin.readline().strip()
all=set()
all.add(t)
if t[0]=='A' and s[0]!='A':
    print(0)
elif t[0]=='A' and s[0]=='A' and t==s+'A'*(len(t)-len(s)):
    print(1)
else:
    for i in range(len(t)-len(s)):
        nowset=set()
        for j in all:
            if j[len(j)-1]=='A':
                nowset.add(j[:len(j)-1])
            if j[0]=='B':
                new=j[::-1]
                nowset.add(new[:len(j)-1])
        all=nowset
    if s in all:
        print(1)
    else:
        print(0)