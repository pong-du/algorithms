# 프로그래머스 
# 홀짝에 따라 다른 값 반환하기 / 181935
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 제출일 : 2024.01.05
def solution(n):
    return sum( i ** (2 - n%2) for i in range(n%2, n+1,2))
# sum 함수, range 함수 간격 기억하기
