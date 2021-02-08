# 백준 2292번 B2
# 벌집
import sys

input = sys.stdin.readline

n = int(input())

def bee(num):

    
    if num == 1:
        return 1
    
    i = 1
    start = 2
    end = 2
    while True:
        start += 6 * (i - 1)
        end += 6 * i
        if start <= num < end:
            return i + 1
        i += 1
print(bee(n))