def solution(new_id):
    answer = ''
    num=['0','1','2','3','4','5','6','7','8','9']
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_id=new_id.lower()
    new_id=list(new_id)
    for i in range(len(new_id)):
        if (new_id[i] in alp) or (new_id[i] in num) or new_id[i]=='-' or new_id[i]=='_' or new_id[i]=='.':
            continue
        else:
            new_id[i]=''
    new_id=''.join(new_id)
    while('..' in new_id):
        new_id=new_id.replace('..','.')
    if len(new_id)!=0 and new_id[0]=='.':
        new_id=new_id[1:]
    if len(new_id)!=0 and new_id[len(new_id)-1]=='.':
        new_id=new_id[:len(new_id)-1]
    if len(new_id)==0:
        new_id='a'
    if len(new_id)>=16:
        new_id=new_id[:15]
        if new_id[len(new_id)-1]=='.':
            new_id=new_id[:len(new_id)-1]
    if len(new_id)<=2:
        laststr=new_id[len(new_id)-1]
        while(len(new_id)<=2):
            new_id+=laststr
    return new_id