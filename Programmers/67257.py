# 프로그래머스 
# 수식 최대화 / 67257
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/67257?language=python3
# 제출일 : 2024.02.25
import re

def solution(expression):
    answer = 0
    fact3 = [['*','+','-'],['*','-','+'],['+','*','-'],['+','-','*'],['-','*','+'],['-','+','*']]
    num_list = re.findall('\d+', expression) # 숫자만
    oper_list = re.findall('\D+', expression) # 연산자만
    priority = list(set(oper_list))

    if len(priority) == 3:
        for temp in fact3:
            answer = max(answer, get_answer(temp, expression))
    elif len(priority) == 2:
        answer = max(answer, get_answer(priority, expression))
        temp = []
        temp.append(priority[1])
        temp.append(priority[0])
        answer = max(answer, get_answer(temp, expression))
    else: # len(priority) == 1
        temp = priority
        answer = max(answer, get_answer(temp, expression))
    return answer

def get_answer(temp_priority, expression):

    temp_num = re.findall('\d+', expression) # 숫자만
    temp_oper = re.findall('\D+', expression) # 연산자만

    for pr in temp_priority:
        idx = 0
        while(1):
            if idx >=  len(temp_oper):
                break
            op = temp_oper[idx]
            if op == pr:
                if op == '+':
                    temp_num[idx] = int(temp_num[idx]) + int(temp_num[idx+1])
                elif op == '-':
                    temp_num[idx] = int(temp_num[idx]) - int(temp_num[idx+1])
                else :
                    temp_num[idx] = int(temp_num[idx]) * int(temp_num[idx+1])

                del temp_oper[idx]
                del temp_num[idx+1]
            else:
                idx += 1
    return abs(int(temp_num[0]))
