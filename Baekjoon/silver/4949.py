# 백준 4949번 S4
# 균형잡힌 세상

while True:
    s = input()
    if s == '.':
        break
    
    cnt = 0
    result = ''
    li = [-1]
    for i in s:
        if i in ['(', '[']:
           li.append(i)
           cnt += 1
        elif i in [')', ']']:
            if li[-1] == '(' and i == ')':
                li.pop()
                cnt -= 1
            elif li[-1] == '[' and i == ']':
                li.pop()
                cnt -= 1
            else:
                cnt += 1
                break
    
    if not cnt:
        result = 'yes'
    else:
        result = 'no'
 
    print(result)

    
    