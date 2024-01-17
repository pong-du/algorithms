# 프로그래머스 
# 성격 유형 검사하기 / 118666
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 제출일 : 2024.01.17
def solution(survey, choices):
    answer = ''
    mbti = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    for i, tp in enumerate(survey):
        score = choices[i] - 4
        if score < 0 : 
            mbti[tp[0]] += score*(-1) 
        else : 
            mbti[tp[1]] += score
    answer += check("R","T",mbti) + check("C","F",mbti) + check("J","M",mbti) + check("A","N",mbti)
    return answer

def check(a, b, dicts):
    if dicts.get(a) >= dicts.get(b):
        return a
    return b
