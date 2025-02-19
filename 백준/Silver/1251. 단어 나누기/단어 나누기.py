import sys
n=sys.stdin.readline().strip()
rev_dict=set()
for i in range(len(n)-2,0,-1):
    for j in range(len(n)-i-1,0,-1):
        now=n[i-1::-1]+n[i+j-1:i-1:-1]+n[:i+j-1:-1]
        rev_dict.add(now)
rev_dict=list(rev_dict)
rev_dict.sort()
print(rev_dict[0])