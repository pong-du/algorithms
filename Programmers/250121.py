# 프로그래머스 
# [PCCE 기출문제] 10번 / 데이터 분석 / 250121
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/250121?language=python3
# 제출일 : 2024.01.02
def solution(data, ext, val_ext, sort_by):
    answer = []
    ext_list = {"code":0, "date":1, "maximum":2, "remain":3}
    
    for item in data : 
        if item[ext_list[ext]] <= val_ext : 
            answer.append(item)
    
    answer.sort(key=lambda item: item[ext_list[sort_by]])

    return answer
