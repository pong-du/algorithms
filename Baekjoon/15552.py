# 백준
# 빠른 A+B / 15552
# 링크 : https://www.acmicpc.net/problem/15552
# 제출일 : 2024.01.01

import sys
N = int(input())
for i in range(N):
	a, b = map(int, sys.stdin.readline().rstrip().split())
	print(a + b)
