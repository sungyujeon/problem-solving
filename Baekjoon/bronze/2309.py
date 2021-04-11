# 백준 2309번 B2
# 일곱 난쟁이

# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline

def calc(_li, _total):
    for i in range(8):
        for j in range(i+1, 9):
            n1 = _li[i]
            n2 = _li[j]
            if _total - n1 - n2 == 100:
                _li.remove(n1)
                _li.remove(n2)
                return _li


# n = 9
li = []
for _ in range(9):
    li.append(int(input()))
total = sum(li)

li = calc(li, total)
li.sort()

for num in li:
    print(num)