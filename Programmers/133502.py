# 프로그래머스 
# 햄버거 만들기 / 133502
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 제출일 : 2024.01.23
def solution(ingredient):
    answer = 0
    idx = 0
    while(idx <= len(ingredient)):
        if ingredient[idx-4:idx] == [1,2,3,1]:
            del ingredient[idx-4:idx]
            idx += -4
            answer += 1
        else:
            idx += 1
    return answer
