# 월코챌 1번

def solution(numbers):
    total = 0

    for i in range(1, 10):
        try:
            r = numbers.index(i)
        except:
            total += i
    return total


numbers = [1, 2, 3, 4, 6, 7, 8, 0]
print(solution(numbers))
