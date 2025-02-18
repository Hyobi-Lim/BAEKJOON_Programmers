import sys
a,b=map(int,sys.stdin.readline().split(' '))
suma=0
sumb=0
while(a>0):
    suma+=a%10
    a//=10
while(b>0):
    sumb+=b%10
    b//=10
print(suma*sumb)