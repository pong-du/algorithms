# 프로그래머스 
# 2023 KAKAO BLIND RECRUITMENT / 개인정보 수집 유효기간 / 150370
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 제출일 : 2024.01.03

## 모든 달은 28일까지 있다는 지문을 제대로 안읽음. 다른 풀이보고 다시 풀었음. 
## 반복문에서 enumerate, 리스트에서 map 기억하기

def to_days(date):
    year, month, day = map(int,date.split('.')) ## 기억하기 : map
    days = year*12*28 + month*28 + day # 모든 달은 28일까지 있다고 가정
    return days
    
def solution(today, terms, privacies):
    answer = []
    terms_list = {}

    for term in terms : # key : value  // 약관종류 : 유효기간 
        terms_list.update({term[0] : int(term[2:])})
    
    for idx, privacy in enumerate(privacies): ## 기억하기 : enumerate
        if to_days(privacy[:-2]) + 28*terms_list[privacy[-1]] <= to_days(today): 
            answer.append(idx+1) # idx만 넣기

    return answer
