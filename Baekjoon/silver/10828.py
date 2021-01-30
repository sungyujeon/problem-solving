# 백준 10828번 S4
# 스택
import sys

def my_push(num):
    stack_list.append(num)

def my_pop():
    if not stack_list:
        return -1
    else:
        return stack_list.pop()

def my_size():
    return len(stack_list)

def my_empty():
    return 0 if stack_list else 1

def my_top():
    if not stack_list:
        return -1
    else:
        return stack_list[-1]


def my_stack(input_query):
    query = input_query[0]
    
    if query == 'push':
        my_push(input_query[1])
    elif query == 'pop':
        print(my_pop())
    elif query == 'size':
        print(my_size())
    elif query == 'empty':
        print(my_empty())
    elif query == 'top':
        print(my_top())
    else:
        return

n = int(sys.stdin.readline().rstrip())
stack_list = []
for _ in range(n):
    query = sys.stdin.readline().rstrip().split()
    my_stack(query)
