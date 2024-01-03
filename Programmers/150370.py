# 프로그래머스 
# 2023 KAKAO BLIND RECRUITMENT / 개인정보 수집 유효기간 / 150370
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 제출일 : 2024.01.03
from datetime import datetime
from dateutil.relativedelta import relativedelta
    
def solution(today, terms, privacies):
    answer = []
    terms_list = {}
    today_dt = datetime.strptime(today, '%Y.%m.%d') # datatime 형식으로 변환

    for term in terms : # key : value  // 약관종류 : 유효기간 
        terms_list.update({term.split()[0] : int(term.split()[1])})
    
    for idx in range(0, len(privacies)):
        temp = privacies[idx].split() # 공백으로 분리 // 날짜 약관종류
        temp_dt = datetime.strptime(temp[0], '%Y.%m.%d') # datatime 형식으로 변환
        temp_month = terms_list[temp[1]] # key 값으로 month 구하기
        if temp_dt + relativedelta(months=temp_month) <= today_dt: 
            answer.append(idx+1) # idx만 넣기

    return answer
