import sys
n=int(sys.stdin.readline())
num0=0
num1=1
for i in range(n-1):
    num0,num1=num0+num1,num0
print(num0+num1)