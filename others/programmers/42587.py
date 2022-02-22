# Programmers
# 프린터

from collections import deque

def solution(priorities, location):
    n = len(priorities)
    priorities = deque(priorities)
    documents = deque([i for i in range(n)])
    cnt = 1

    while True:
        currPriority = priorities.popleft()
        currDocument = documents.popleft()

        higherFlag = hasHigherPriority(currPriority, priorities)
        if higherFlag:
            priorities.append(currPriority)
            documents.append(currDocument)
        else:
            if currDocument == location:
                break
            cnt += 1
    
    return cnt

    
def hasHigherPriority(curr, priorities):
    n = len(priorities)
    for i in range(1, n):
        if (priorities[i] > curr):
            return True
    return False

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))