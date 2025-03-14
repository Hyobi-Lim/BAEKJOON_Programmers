import sys
n=int(sys.stdin.readline())
num=666
count=1
while(count!=n):
    num+=1
    if '666' in str(num):
        count+=1
print(num)