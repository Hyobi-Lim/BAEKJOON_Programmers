import sys
from itertools import permutations
n=int(sys.stdin.readline())
k=int(sys.stdin.readline())
num=[]
num_set=set()
for i in range(n):
    num.append(sys.stdin.readline().strip())
for i in permutations(num,k):
    num_set.add(''.join(list(i)))
print(len(num_set))