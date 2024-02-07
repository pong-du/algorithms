# 프로그래머스 
# 리코쳇 로봇 / 169199
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 제출일 : 2024.02.08
from collections import deque
dx, dy = [0,1,0,-1], [1,0,-1,0]

def solution(board):
    answer = None
    rows = len(board)
    cols = len(board[0])
    visited = [[False for j in range(cols)] for i in range(rows)]
    answers = [[0 for j in range(cols)] for i in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start = [i,j]
                answers[i][j] = 0
    answer = bfs(board, start, visited, answers)

    if answer is None: 
        answer = -1
    return answer

def bfs(board, start, visited, answer):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    
    while(queue):
        v = queue.popleft()  
        if board[v[0]][v[1]] == 'G':
            return answer[v[0]][v[1]]

        for i in range(0,4):
            tmp_x = v[0]
            tmp_y = v[1]
            item = v
            while(1):
                if (tmp_x+dx[i] < 0 or tmp_x+dx[i] == len(board)) or (tmp_y+dy[i] < 0 or tmp_y+dy[i] == len(board[0])): 
                    item = [tmp_x, tmp_y]
                    break  
                if (board[tmp_x+dx[i]][tmp_y+dy[i]] == 'D'): 
                    item = [tmp_x, tmp_y]
                    break 
                tmp_x += dx[i]
                tmp_y += dy[i]
            
            if not visited[item[0]][item[1]] :
                queue.append(item)
                answer[item[0]][item[1]] = answer[v[0]][v[1]] + 1
                visited[item[0]][item[1]] = True