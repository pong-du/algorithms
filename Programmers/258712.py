# 프로그래머스 
# 가장 많이 받은 선물 / 258712
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258712
# 제출일 : 2024.01.22
def solution(friends, gifts):
    answer = 0
    friend_dict = dict()
    for friend in friends:
        friend_dict[friend] ={v : 0 for v in friends}
        friend_dict[friend]['idx'] = 0 # 선물 지수

    for gift in gifts:
        frm, to = gift.split()
        friend_dict[frm][to] += 1
        friend_dict[frm]['idx'] += 1
        friend_dict[to]['idx'] += -1
        
    for to in friends:
        cnt = 0
        for frm in friends:
            if to != frm:
                if friend_dict[to][frm] == friend_dict[frm][to]:
                    if friend_dict[to]['idx'] > friend_dict[frm]['idx'] : 
                        cnt += 1
                elif friend_dict[to][frm] > friend_dict[frm][to]: 
                    cnt += 1
        answer = max(answer, cnt)
                
    return answer
