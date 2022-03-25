# Programmers
# 가장 큰 수 sort

#### 효율성3
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

#### 효율성2
def solution(numbers):
    # '0'
    num_set = set(numbers)
    if len(num_set) == 1 and num_set.pop() == 0:
        return '0'

    numbers = list(map(lambda num: [(str(num) * 3)[:4], len(str(num))], numbers))
    numbers.sort(reverse=True)

    numbers = list(map(lambda val: val[0][:val[1]], numbers))
    return ''.join(numbers)

#### 효율성1 (fail testcase 1~6)
from collections import deque

def recur(numbers, base):
    ans = []
    while numbers:
        _len = len(numbers)

        # left only 1
        if _len == 1:
            ans.append(numbers.pop())
            continue
        
        # len == 1
        number_0 = numbers[0]
        number_1 = numbers[1]
        if number_0[0] > number_1[0]:
            ans.append(numbers.popleft())
            continue
        
        # len > 1   1 10 100
        tmp_numbers = []
        while numbers:
            if numbers[0][0] == number_0[0]:
                tmp_numbers.append(numbers.popleft())
            else:
                break
        
        left = deque([])
        center = []
        right = deque([])

        # base number
        _base = tmp_numbers[0][0]
        if _base != '0':
            base = _base

        for tn in tmp_numbers:
            if len(tn) == 1:
                center.append(tn)
            else:
                if base < tn[1]:
                    left.append(tn[1:])
                elif base > tn[1]:
                    right.append(tn[1:])
                else:  # base == tn[1]
                    if len(tn) > 2 and base < tn[2]:
                        left.append(tn[1:])
                    else:
                        right.append(tn[1:])


        left = list(map(lambda val: tn[0] + val, recur(left, base)))
        right = list(map(lambda val: tn[0] + val, recur(right, base)))
        tmp_numbers = left + center + right

        ans += tmp_numbers
    return ans

# def solution(numbers):
#     numbers = deque(sorted(list(map(str, numbers)), reverse=True))
    
#     # '0'
#     num_set = set(numbers)
#     if len(num_set) == 1 and num_set.pop() == '0':
#         return '0'
    
#     return ''.join(recur(numbers, numbers[0][0]))

#### 정확성
# from itertools import permutations

# def solution(numbers):
#     candidates = []
#     n = len(numbers)

#     perms = list(permutations(numbers, n))
#     for perm in perms:
#         num = int(''.join(list(map(str, perm))))
#         candidates.append(num)

#     return str(max(candidates))

numbers = [1, 0, 10, 100, 1000]
numbers = [0, 0, 1000, 0]
numbers = [9, 998]
print(solution(numbers))