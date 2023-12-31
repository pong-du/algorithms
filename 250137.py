# 프로그래머스 
# [PCCP 기출문제] 1번 / 붕대 감기 / 250137
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/250137?language=python3
# 제출일 : 2024.01.01

def solution(bandage, health, attacks):
    answer = 0
    current_health = health 
    t, x, y = bandage # 시전 시간, 초당 회복량, 추가 회복량
    
    # 마지막 공격시간 체크 
    max_time = attacks[-1][0]
    
    # attacks 리스트를 순차로 가져오기 위함
    attacks_idx = len(attacks)
    attacks_cnt = 0
    
    # 연속 붕대감기 시간 
    stream_time = 0
    
    # 시간 순서 대로 체력 확인(0 ~ max_time)
    for current_time in range(0, max_time + 1):
        attack_time, damage = attacks[attacks_cnt]
        
        # 공격 O   
        if current_time == attack_time :
            # 피해량(damage) 만큼 체력 감소   
            current_health = current_health - damage
            # 공격을 받는 경우, 연속 시전시간 초기화  
            stream_time = 0
            attacks_cnt += 1
        # 공격 X  
        else : 
            # 연속 시전시간 + 1 
            stream_time += 1
            # 초당 회복량(x)만큼 체력 회복
            current_health += x

            # 연속 시전 시간 == 시전 시간(t)일 때
            if stream_time == t :
                current_health = current_health + y
                # 연속 시전시간 초기화  
                stream_time = 0
            # 최대 체력 이상 회복은 불가 
            if current_health > health :
                current_health = health
        
        if current_health <= 0 : 
            return -1 
    
    answer = current_health
    
    return answer
