import sys,math
def primenumber(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True			
n=int(sys.stdin.readline())
student=[]
studentnum=dict()
studentprime=dict()
studentprimecount=dict()
for i in range(n):
    num=int(sys.stdin.readline())
    student.append(num)
    if num in studentnum:
        studentnum[num]+=1
    else:
        studentnum[num]=1
        studentprime[num]=set()
        studentprimecount[num]=0
        for j in range(1,int(math.sqrt(num))+1):
            if num%j==0:
                studentprime[num].add(j)
                studentprime[num].add(num//j)
for i in studentprimecount:
    for j in studentprime[i]:
        if j in studentnum:
            studentprimecount[i]+=studentnum[j]
for i in student:
    print(studentprimecount[i]-1)