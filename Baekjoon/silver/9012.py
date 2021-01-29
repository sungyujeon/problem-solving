# 백준 9012번
# 괄호

# 1. (가 들어가면 list에 append()
# 2. )가 들어가면 list에서 pop()
# 3. list가 비어있으면 "YES" 아니면 "NO"
import sys

n = int(sys.stdin.readline())

parenthesis_list = []
for _ in range(n):
    parenthesis_list.append(sys.stdin.readline().strip())


def check(parenthesis):
    parenthesis_check = []
    result = ''
    for p in parenthesis:
        if parenthesis[0] == ')':
           return 'NO' 
        else:    
            if p == '(':
                parenthesis_check.append(p)
            else:
                if not len(parenthesis_check):
                    return 'NO'
                parenthesis_check.pop()
                
    return 'NO' if parenthesis_check else 'YES'
    
for parenthesis in parenthesis_list:
   print(check(parenthesis))