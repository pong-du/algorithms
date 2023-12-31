# 백준
# 알람시계 / 2884
# 링크 : https://www.acmicpc.net/problem/2884
# 제출일 : 2024.01.01

x, y = map(int, input().split())
if x == 0 and y < 45 : x = 24
result = x * 60 + y - 45
print(f"{int(result/60)} {result%60}")
