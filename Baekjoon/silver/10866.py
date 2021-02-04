# 백준 10866번 S4
# 덱

import sys
input = sys.stdin.readline

li = []
def push_back(num):
    li.append(num)
def push_front(num):
    li.insert(0, num)
def pop_front():
    if not li:
        return -1
    else:
        number = li[0]
        del li[0]
        return number
def pop_back():
    if not li:
        return -1
    else:
        number = li[len(li)-1]
        del li[len(li)-1]
        return number
def size():
    return len(li)
def empty():
    return 1 if not li else 0
def front():
    return -1 if not li else li[0]
def back():
    return -1 if not li else li[len(li)-1]

def deque(query):
    querys = query.split()
    query = querys[0]

    if query == 'push_front':
        push_front(querys[1])
    elif query == 'push_back':
        push_back(querys[1])
    elif query == 'pop_front':
        print(pop_front())
    elif query == 'pop_back':
        print(pop_back())
    elif query == 'size':
        print(size())
    elif query == 'empty':
        print(empty())
    elif query == 'front':
        print(front())
    elif query == 'back':
        print(back())
    else:
        return

n = int(input())
for _ in range(n):
    deque(input())