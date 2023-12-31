# 백준
# 오븐 시계 / 2525
# 링크 : https://www.acmicpc.net/problem/2525
# 제출일 : 2024.01.01

A, B = map(int, input().split())
C = int(input())
result = A*60 + B + C
print(f"{int(result/60) % 24} {result%60}")
