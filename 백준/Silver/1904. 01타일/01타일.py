import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
bi=[1,2]
for i in range(2,n):
    bi.append((bi[i-1]+bi[i-2])%15746)
print(bi[n-1])