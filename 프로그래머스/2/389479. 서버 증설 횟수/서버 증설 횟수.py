def solution(players, m, k):
    answer = 0
    now_server=0
    server_end_time=dict()
    for i in range(24):
        if i in server_end_time:
            now_server-=server_end_time[i]
        need_server=players[i]//m
        if need_server>now_server:
            answer+=(need_server-now_server)
            server_end_time[i+k]=(need_server-now_server)
            now_server=need_server
    return answer