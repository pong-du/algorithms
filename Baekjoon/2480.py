# 백준
# 주사위 세개 / 2480
# 링크 : https://www.acmicpc.net/problem/2480
# 제출일 : 2024.01.01

result = list(map(int, input().split()))
result.sort()

if result[0] == result[1] == result[2] : 
	print(10000 + result[0]*1000)
elif result[0] == result[1] or result[1] == result[2]:
	print(1000 + result[1]*100)
else :
	print(result[2]*100)
