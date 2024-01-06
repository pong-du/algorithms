# 프로그래머스
# 하노이의 탑 / 12946
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12946
# 제출일 : 2024.01.06
def solution(n):
    return hanoi(n, 1, 3, 2, [])

def move(start, dest, result):
    result.append([start, dest])
    return result

def hanoi(n, start, dest, via, result): # 시작기둥, 목적기둥, 보조기둥
    if n <= 1:
        move(start, dest, result) # 1개가 남았을 때는 start -> dest로 바로 옮기기
        return
    hanoi(n-1, start, via, dest, result) # n-1 개의 원반을 dest 기둥을 이용하여 via 로 옮기기
    result = move(start, dest, result) # n-1 개를 via 로 보내놓고, n 원반을 dest로 옮기기
    hanoi(n-1, via, dest, start, result) # n-1 개의 원반을 start 기둥을 이용하여 dest 로 옮기기
    return result
