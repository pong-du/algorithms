# 프로그래머스 
# 글자 이어 붙여 문자열 만들기 / 181915
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 제출일 : 2024.01.05
def solution(my_string, index_list):
    return ''.join([my_string[index_list[i]] for i in range(len(index_list))])
