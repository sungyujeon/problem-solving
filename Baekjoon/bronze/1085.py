# 백준 1085번 B3
# 직사각형에서 탈출
import sys

x, y, w, h = map(int, sys.stdin.readline().split())

def close(x, y):
    min_x = x if w - x >= w / 2 else w - x
    min_y = y if h - y >= h / 2 else h - y
    return min(min_x, min_y)

print(close(x, y))