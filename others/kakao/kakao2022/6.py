# 카카오 블라인드 2022 6번

from pprint import pprint


def setBoard(board, t, si, sj, ei, ej, degree):
    if t == 1:
        for i in range(si, ei+1):
            for j in range(sj, ej+1):
                board[i][j] -= degree
    else:
        for i in range(si, ei+1):
            for j in range(sj, ej+1):
                board[i][j] += degree


def solution(board, skill):
    col = len(board)
    row = len(board[0])

    for sk in skill:
        sType, si, sj, ei, ej, degree = sk
        setBoard(board, sType, si, sj, ei, ej, degree)

    total = 0
    for i in range(col):
        for j in range(row):
            if board[i][j] > 0:
                total += 1

    return total


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2],
         [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))
