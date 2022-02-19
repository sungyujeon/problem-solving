# Programmers
# 기능개발

from collections import deque

def solution(progress, speeds):
    answer = []
    progress = deque(progress)
    speeds = deque(speeds)
    n = len(progress)

    while progress:
        
        for i in range(len(progress)):
            if progress[i] == True:
                continue

            progress[i] += speeds[i]
            if progress[i] >= 100:
                progress[i] = True
        
        cnt = 0
        if progress[0] == True:
            while progress:
                curr_progress = progress[0]
                if curr_progress == True:
                    cnt += 1
                    progress.popleft()
                    speeds.popleft()
                else:
                    break
        
        if cnt > 0:
            answer.append(cnt)
            
    return answer


progress = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progress, speeds))