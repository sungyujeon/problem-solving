# 백준 10250번 B3
# ACM 호텔
import sys

T = int(sys.stdin.readline().strip())


def arrange(h, n):
    # 'xx호' (n // h) + 1 (호)
    # 'yy층' (n % h) (층)
    floor = 0
    floor = (n % h) * 100 if n % h else h * 100

    ho = (n // h) + 1 if n % h else n // h
    
    room_number = floor + ho
    return room_number

for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().strip().split())
    print(arrange(h, n))