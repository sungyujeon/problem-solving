# 백준 10845번 S4
# 큐

import sys
input = sys.stdin.readline

li = []
def push(num):
    li.append(num)
def pop():
    if not li:
        return -1
    else:
        number = li[0]
        del li[0]
        return number
def size():
    return len(li)
def empty():
    return 1 if not li else 0
def front():
    return -1 if not li else li[0]
def back():
    return -1 if not li else li[len(li)-1]

def queue(query):
    querys = query.split()
    query = querys[0]

    if query == 'push':
        push(querys[1])
    elif query == 'pop':
        print(pop())
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
    queue(input())
