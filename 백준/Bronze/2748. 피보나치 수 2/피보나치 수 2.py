import sys
n=int(sys.stdin.readline())
answer=[0,1]
for i in range(n-1):
    answer.append(answer[i]+answer[i+1])
print(answer[-1])