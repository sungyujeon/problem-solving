# 백준 10816번 S4
# 숫자 카드 2

import sys
input = sys.stdin.readline

_ = input()
N = sorted(map(int, input().split()))
_ = input()
M = map(int, input().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    mid = (start+end) // 2
    if n == N[mid]:
        pass




# import sys
# input = sys.stdin.readline
# n = int(input())
# cards = list(map(int, input().split()))
# cards.sort()

# m = int(input())
# check_nums = list(map(int, input().split()))
# check_nums2 = sorted(check_nums)

# def count(number):
#     global cards
#     cnt = 0
#     for idx, card_num in enumerate(cards):
#         if number == card_num:
#             cnt += 1
#         elif number < card_num:
#             cards = cards[idx:]
#             return cnt
#     return cnt

# result = []
# for num in check_nums2:
#     result.append(str(count(num)))

# results = dict(zip(check_nums2, result))

# r = []
# for check_num1 in check_nums:
#     r.append(str(results.get(check_num1)))
# print(' '.join(r))