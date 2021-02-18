# 백준 10799번 S3
# 쇠막대기

import sys

input = sys.stdin.readline

brackets = input().strip()
bar = 1  # 쇠막대기
result = 0  # 막대기 갯수

for i in range(1, len(brackets)): 
    if brackets[i] == '(':  # 여는 괄호일 때 bar 추가
        bar += 1
    else:  # 닫는 괄호 일 때
        if brackets[i-1] == '(':  # 이전 괄호가 여는 괄호였으면 레이저이기 때문에 bar-- & 현재 bar만큼 result 추가
            bar -= 1
            result += bar
        else:  # 닫는괄호 다음 닫는 괄호이기 때문에 bar-- & result++
            bar -= 1
            result += 1

print(result)