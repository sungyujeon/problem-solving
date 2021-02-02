# 백준 2164번 S4
# 카드2
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.pop())




# def card(n):
#     for i in range(1, 20):
#         if 2 ** (i - 1) <= n < 2 ** i:
#             return 2 ** (i - 1)
# print(card(n))




# def exp(n):
#     c = 0
#     while n > 1:
#         n = n // 2
#         c += 1
#     return c

# def card(n):
#     return 2 ** exp(n)

# print(card(n))




# def discard(cards):
#     while len(cards) != 1:
#         cards.pop(0)
#         cards.append(cards.pop(0))
#     return cards

# print(discard(cards)[0])

# def discard(cards):
#     while len(cards) != 1:
#         cards = [v for i, v in enumerate(cards) if i % 2]
#     return cards

# print(discard(card))