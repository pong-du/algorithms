# 프로그래머스 
# 바탕화면 정리 / 161990
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 제출일 : 2024.01.20
def solution(wallpaper):
    answer = []
    min_x,min_y = (50,50)
    max_x,max_y = (0,0)
    
    for idx, row in enumerate(wallpaper):
        if row.find('#') >= 0:
            min_y = min(min_y, row.find('#'))
            max_y = max(max_y, len(row) - row[::-1].find('#'))
            min_x = min(min_x, idx)
            max_x = max(max_x, idx+1)
    return [min_x, min_y, max_x, max_y]
