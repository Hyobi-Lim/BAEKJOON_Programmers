def solution(routes):
    routes.sort(key=lambda x: x[1])  # 종료 지점 기준으로 정렬
    answer = 0
    camera_position = -30001  # 카메라 위치를 초기화
    
    for route in routes:
        # 현재 경로의 시작 지점이 이전 카메라 위치보다 크면 새로운 카메라가 필요
        if camera_position < route[0]:
            camera_position = route[1]  # 새로운 카메라를 현재 경로의 종료 지점에 설치
            answer += 1

    return answer
