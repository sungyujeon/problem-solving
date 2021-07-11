# 백준 20436번 S4
# ZOAC 3
# sys.stdin = open('input.txt', 'r')

import sys
input = sys.stdin.readline

left = set(['q','w','e','r','t','a','s','d','f','g','z','x','c','v'])

keyboard = [
    ['q','w','e','r','t','y','u','i','o','p',],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
]
locations = [[] for _ in range(26)]
for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        idx = ord(keyboard[i][j]) - 97
        locations[idx] = (i, j)

def alphabetToAscii(alphabet):
    return ord(alphabet) - 97

def calcTime(cx, cy, nx, ny):
    return abs(cx-nx) + abs(cy-ny)

def solution(l, r, w):
    curr_lx, curr_ly = locations[alphabetToAscii(l)]
    curr_rx, curr_ry = locations[alphabetToAscii(r)]
    total = 0

    for alpha in w:
        next_x, next_y = locations[alphabetToAscii(alpha)]
        if alpha in left:
            total += calcTime(curr_lx, curr_ly, next_x, next_y)
            curr_lx, curr_ly = next_x, next_y
        else:
            total += calcTime(curr_rx, curr_ry, next_x, next_y)
            curr_rx, curr_ry = next_x, next_y

    return total
            

l_start, r_start = input().rstrip().split()
word = input().rstrip()
res = solution(l_start, r_start, word)
res += len(word)

print(res)