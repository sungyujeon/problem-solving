# 백준 18222번 S1
# 투에모스 문자열

import sys
input = sys.stdin.readline

# def setNums(nums):
#     newNums = list(nums)
#     for i in range(len(newNums)):
#         if newNums[i] == '0':
#             newNums[i] = '1'
#         else:
#             newNums[i] = '0'

#     return newNums

# def thueMorse(k):
#     i = 0
#     K = 1
#     nums = '0'

#     while K < k:
#         nums += ''.join(setNums(nums))
#         i += 1
#         K = 2 ** i

#     # 이전까지의 K
#     if i > 0:
#         K = 2 ** (i - 1)

#     return nums[k - K - 1]

def recursive(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1

    if k % 2:
        return 1 - recursive(k // 2)
    else:
        return recursive(k // 2)

k = int(input())
print(recursive(k-1))

# T = 0
# while T < 3:
#     k = int(input())
#     print(thueMorse(k))
#     T += 1

