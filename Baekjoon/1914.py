# 백준
# 하노이 탑 / 1914
# 링크 : https://www.acmicpc.net/problem/1914
# 제출일 : 2024.01.06

n = int(input())

def move(start, dest, result):
    result.append([start, dest])
    return result

def hanoi(n, start, dest, via, result):
    if n <= 1: 
        move(start, dest, result)
        return ;
    hanoi(n-1, start, via, dest, result)
    result = move(start, dest, result)
    hanoi(n-1, via, dest, start, result)
    return result

print(2**n -1)

if n <= 20:
    result = hanoi(n, 1, 3, 2, [])
    for item in result: print(f"{item[0]} {item[1]}" )
