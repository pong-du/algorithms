# 프로그래머스
# 문자열 나누기 / 140108
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 제출일 : 2024.01.10
def solution(s):
    answer = 0
    xx = s[0]
    x_cnt = 0
    y_cnt = 0
    for idx, item in enumerate(s):
        if item == xx : 
            x_cnt += 1
        else : 
            y_cnt += 1
        if x_cnt == y_cnt :
            answer += 1
            x_cnt = 0
            y_cnt = 0
            if idx + 1 != len(s): 
                xx = s[idx+1]
        else : 
            if idx + 1 == len(s):
                answer += 1
    return answer
