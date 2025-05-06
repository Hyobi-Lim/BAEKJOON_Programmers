import sys
n,m=map(int,sys.stdin.readline().split())
dna=[]
for i in range(n):
    dna.append(list(sys.stdin.readline().strip()))
answer_dna=''
answer_num=0
for i in range(m):
    dna_check={'A':0,'C':0,'G':0,'T':0}
    for j in range(n):
        dna_check[dna[j][i]]+=1
    dna_max=max(dna_check.values())
    for j in dna_check:
        if dna_check[j]==dna_max:
            answer_dna+=j
            answer_num+=(n-dna_max)
            break
print(answer_dna)
print(answer_num)