# 백준 11899번 S4
# 괄호 끼워넣기
# sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
        
brackets = list(input())

openStack = []
close = 0
for bracket in brackets:
    if bracket == '(':
        openStack.append(bracket)
    elif bracket == ')':
        if openStack:
            openStack.pop()
        else:
            close += 1

result = close + len(openStack)
print(result)