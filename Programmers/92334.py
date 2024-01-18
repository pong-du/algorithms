# 프로그래머스 
# 신고 결과 받기 / 92334
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 제출일 : 2024.01.18
def solution(id_list, report, k):
    answer = []
    id_dict = {id : [] for id in id_list} # 요런식으로도 선언 가능
    reported = {id : 0 for id in id_list}
    report_distinct= list(set(report)) # 중복 제거 : 동일한 유저에 대한 신고 횟수는 1회로 처리
    
    for user_str in report_distinct: # O(n) : 시간 복잡도 고려하기 n <= 20,000
        user1, user2 = user_str.split()
        id_dict[user1].append(user2)
        reported[user2] += 1
        
    for report_users in id_dict.values() : # O(n^2) : 시간 복잡도 고려하기 n*n <= 1,000*?? 
        cnt = 0
        for user in report_users:
            if reported[user] >= k : 
                cnt += 1
        answer.append(cnt)
    return answer
