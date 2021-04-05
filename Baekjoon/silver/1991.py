# 백준 1991번 S1
# 트리 순회

import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')


def inorder(_node, _ch1, _ch2):
    if _ch1[_node] == 0 and _ch2[_node] == 0:
        char = chr(_node + 64)
        print(char, end='')
        return
    
    left_child = _ch1[_node]
    right_child = _ch2[_node]
    
    if left_child != 0:
        inorder(left_child, _ch1, _ch2)

    char = chr(_node + 64)
    print(char, end='')
    
    if right_child != 0:
        inorder(right_child, _ch1, _ch2)

def preorder(_node, _ch1, _ch2):
    if _ch1[_node] == 0 and _ch2[_node] == 0:
        char = chr(_node + 64)
        print(char, end='')
        return
    
    left_child = _ch1[_node]
    right_child = _ch2[_node]
    
    char = chr(_node + 64)
    print(char, end='')

    if left_child != 0:
        preorder(left_child, _ch1, _ch2)
    
    if right_child != 0:
        preorder(right_child, _ch1, _ch2)


def postorder(_node, _ch1, _ch2):
    if _ch1[_node] == 0 and _ch2[_node] == 0:
        char = chr(_node + 64)
        print(char, end='')
        return
    
    left_child = _ch1[_node]
    right_child = _ch2[_node]
    

    if left_child != 0:
        postorder(left_child, _ch1, _ch2)
    
    if right_child != 0:
        postorder(right_child, _ch1, _ch2)

    char = chr(_node + 64)
    print(char, end='')

n = int(input())
ch1 = [0] * 27
ch2 = [0] * 27

for _ in range(n):
    a, b, c = input().split()
    a = ord(a) - 64
    b = ord(b) - 64 if b != '.' else 0
    c = ord(c) - 64 if c != '.' else 0

    
    ch1[a] = b
    ch2[a] = c

preorder(1, ch1, ch2)
print()
inorder(1, ch1, ch2)
print()
postorder(1, ch1, ch2)
    