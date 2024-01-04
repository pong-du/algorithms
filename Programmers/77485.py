# 프로그래머스 
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) / 행렬 테두리 회전하기 / 77485
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/77485
# 제출일 : 2024.01.04
def solution(rows, columns, queries):
    answer = []
    arr = [[i*columns + j + 1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        st_row, st_col, ed_row, ed_col = query
        # dir = {'R':(0,1),'D':(1,0),'L':(0,-1),'U':(-1,0)}        
        dir = [[0,1]]*(ed_col-st_col) + [[1,0]]*(ed_row-st_row) + [[0,-1]]*(ed_col-st_col) + [[-1,0]]*(ed_row-st_row)
        
        min_num = rows*columns
        row = st_row-1
        col = st_col-1
        
        before = arr[row][col]
        
        for idx in range(0, len(dir)) :
            min_num = min(min_num, before)
            
            after = arr[row + dir[idx][0]][col + dir[idx][1]]
            arr[row + dir[idx][0]][col + dir[idx][1]] = before
            
            row +=  dir[idx][0]
            col += dir[idx][1]
            
            before = after     
        
        answer.append(min_num)
            
    return answer
