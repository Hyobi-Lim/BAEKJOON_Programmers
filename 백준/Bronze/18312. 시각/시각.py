import sys
n,k=map(int,sys.stdin.readline().split())
k=str(k)
answer=0
for a in range(n+1):
    for b in range(60):
        for c in range(60):
            if k=='0':
                if a<10 or b<10 or c<10:
                    answer+=1
                    continue
            if k in str(a) or k in str(b) or k in str(c):
                answer+=1
print(answer)
