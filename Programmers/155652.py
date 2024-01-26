# 프로그래머스 
# 둘만의 암호 / 155652
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 제출일 : 2024.01.26
import re
import string

def solution(s, skip, index):
    answer = ''
    alpha = string.ascii_lowercase # [a-z] list 
    context = re.findall(re.compile('[^'+skip+']'), alpha) # skip 할 문자 정규표현식으로 제외
    answer += context[(context.index(t) + index)%len(context)] for t in s
		for tmp in s : 
        answer += context[(context.index(tmp) + index)%len(context)]
    return answer

# 컴프리헨션 문법으로 이렇게 표현 가능. 윗 쪽이 더 가독성이 좋은 것 같다.
"""
def solution(s, skip, index):
    alpha = string.ascii_lowercase # [a-z] list 
    context = re.findall(re.compile('[^'+skip+']'), alpha) # skip 할 문자 정규표현식으로 제외
    return ''.join([context[(context.index(t) + index)%len(context)] for t in s])
"""
