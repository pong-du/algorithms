# 프로그래머스 
# 숫자 짝궁 / 131128
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 제출일 : 2024.01.28
def solution(X, Y):
    answer = ''
    tmp1 = sorted(X, reverse=True) # O(nlogn)
    tmp2 = sorted(Y, reverse=True) # O(mlogm)
    n,m = (0,0)
    while(1): # O(m+n)
        if n == len(tmp1) or m == len(tmp2) or answer == '0': break
        if tmp1[n] == tmp2[m]:
            answer += tmp1[n]
            n += 1
            m += 1
        elif tmp1[n] < tmp2[m] : m += 1
        else : n += 1
    
    if answer == "": answer = '-1'    
    return answer
