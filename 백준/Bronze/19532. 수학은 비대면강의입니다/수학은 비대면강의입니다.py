import sys
a,b,c,d,e,f=list(map(int,sys.stdin.readline().split()))
x=y=0
if 0 in [a,b,d,e]:
    if a==0:
        y=c//b
        x=(f-e*y)//d
    elif b==0:
        x=c//a
        y=(f-d*x)//e
    elif d==0:
        y=f//e
        x=(c-b*y)//a
    else:
        x=f//d
        y=(c-a*x)//b
elif abs(a)==abs(d):
    if a==d:
        y=(c-f)//(b-e)
    else:
        y=(c+f)//(b+e)
    x=(c-b*y)//a
elif abs(b)==abs(e):
    if b==e:
        x=(c-f)//(a-d)
    else:
        x=(c+f)//(a+d)
    y=(c-a*x)//b
else:
    num=a*d
    num1=num//a
    num2=num//d
    a*=num1
    b*=num1
    c*=num1
    d*=num2
    e*=num2
    f*=num2
    if a==d:
        y=(c-f)//(b-e)
    else:
        y=(c+f)//(b+e)
    x=(c-b*y)//a
print(x,y)