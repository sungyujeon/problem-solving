# Programmers
# 정렬

def solution(array, commands):
    answer = []

    for command in commands:
        new_array = list(array)
        start, end, idx = command
        new_array = new_array[start-1:end]
        new_array.sort()
        answer.append(new_array[idx-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
