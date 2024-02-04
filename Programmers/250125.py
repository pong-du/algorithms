# 프로그래머스 
# 이웃한 칸 / 250125
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/250125
# 제출일 : 2024.02.04
def solution(board, h, w):
    answer = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    N = len(board)
    for i in range(0,4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (h_check < N and h_check >= 0) and (w_check < N and w_check >= 0):
            if board[h][w] == board[h_check][w_check]:
                answer += 1

    return answer