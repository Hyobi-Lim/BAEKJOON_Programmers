import sys
n=int(sys.stdin.readline())
answer=[[' ']*(n*4-3) for _ in range(n*4-3)]
for i in range(n):
    x=2*i
    y=2*i
    for j in range((n-i)*4-3):
        answer[x][y+j]='*'
        answer[x+j][y]='*'
        answer[x+j][y+(n-i)*4-4]='*'
        answer[x+(n-i)*4-4][y+j]='*'
for j in answer:
    print(''.join(j))