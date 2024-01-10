# 프로그
# 3번 뒤집기 / 68935
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 제출일 : 2024.01.10
def solution(n):
    temp = ''
    answer = 0
    while(1):
        if n < 3 : 
            temp += str(n)
            break
        temp += str(n % 3) 
        n = int(n / 3)
        
    for i, item in enumerate(temp):
        answer += int(item) * ( 3 ** (len(temp) - i - 1))
    return answer
