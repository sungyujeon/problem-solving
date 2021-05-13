numbers = [2, 7]
answer = []

for number in numbers:
    num = list(bin(number))
    flag = False
    last_idx = len(num)-1

    for i in range(last_idx, 1, -1):
        if num[i] == '0':
            if i == last_idx:
                num[i] = '1'
            else:
                num[i] = '1'
                num[i+1] = '0'
            
            flag = True
            num = int(''.join(num), 2)
            break
    if not flag:
        num.append('1')
        num[3] = '0'
        num = int(''.join(num), 2)
    
    answer.append(num)
print(answer)



# def f(s):
#     cnt = 0
#     for i in range(len(s)):
#         if s[i] == '1':
#             cnt += 1
#         if cnt > 2:
#             return False
#     return True

# for number in numbers:
#     _n = number
#     while True:
#         _n += 1
#         bin_res = bin(number ^ _n)
        
#         if f(bin_res):
#             break
#     answer.append(_n)
# print(answer)



# def f(s):
#     global n
    
#     i = len(s) - 1
#     cnt = 0
#     tmp_n = list(n)
#     while tmp_n:
#         char = tmp_n.pop()
#         if char != s[i]:
#             cnt += 1
#         i -= 1
    
#     cnt += i + 1

#     if cnt < 3:
#         return True

#     return False

# for number in numbers:
#     n = list(bin(number)[2:])
#     _n = number
#     while True:
#         _n += 1
#         if f(list(bin(_n)[2:])):
#             break
#     answer.append(_n)

# print(answer)