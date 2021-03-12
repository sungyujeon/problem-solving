import sys

for i in range(1, 1 << 3):
    for j in range(3):
        if i & (1 << j):
            print()