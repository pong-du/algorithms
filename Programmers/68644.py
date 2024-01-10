# 프로그래머스
# 두 개 뽑아서 더하기 / 68644
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 제출일 : 2024.01.10
def solution(numbers):
    answer = []
    for i, num_i in enumerate(numbers[0:-1]):
        for j, num_j in enumerate(numbers[i+1:]):
            if num_i + num_j not in answer:
                answer.append(num_i + num_j)
    answer = sorted(answer)
    return answer
