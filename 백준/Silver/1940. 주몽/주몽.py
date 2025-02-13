N=int(input())
M=int(input())
materials=list(map(int,input().split()))
materials.sort()
materials_dict=dict()
answer=0
for i in materials:
    if i in materials_dict:
        materials_dict[i]+=1
    else:
        materials_dict[i]=1
for i in materials_dict:
    if i>M//2:
        break
    elif M%2==0 and i==M//2:
        answer+=materials_dict[i]//2
    else:
        if M-i in materials_dict:
            answer+=min(materials_dict[i],materials_dict[M-i])
print(answer)