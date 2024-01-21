# 프로그래머스 
# 달리기 경주 / 178871
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 제출일 : 2024.01.21
def solution(players, callings):
    aa = {k:v for v,k in enumerate(players)} 
    for user in callings :
        idx = int(aa[user])  # dict 타입일 때 O(1)
        front_user = players[idx-1]
        aa[front_user], aa[user] = idx, idx-1
        players[idx-1], players[idx] = user, front_user
    return players
