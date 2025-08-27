def solution(cards):
    answer = 0
    card_boolean=[False]*len(cards)
    card_list_len=[]
    for i in range(len(cards)):
        if(not card_boolean[i]):
            idx=i
            cnt=0
            while(not card_boolean[idx]):
                card_boolean[idx]=True
                idx=cards[idx]-1
                cnt+=1
            card_list_len.append(cnt)
    card_list_len.sort()
    if len(card_list_len)==1:
        return 0
    return card_list_len[-1]*card_list_len[-2]