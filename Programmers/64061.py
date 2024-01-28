# 프로그래머스 
# 크레인 인형뽑기 게임 / 64061
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 제출일 : 2024.01.28
def solution(board, moves):
    answer = 0
    stack = []
    arr = {}
    for idx, row in enumerate(board[::-1]):
        for col, val in enumerate(row): 
            if idx == 0 : arr[col+1] = []
            if val != 0:
                arr[col+1].append(val)

    for col in moves:
        if len(arr[col]) == 0 : continue
        item = arr[col].pop()
        if len(stack) > 0 :
            top = stack[-1]
            if top == item :
                stack.pop()
                answer += 2 
                continue       
        stack.append(item)       
    return answer
