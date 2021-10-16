from pprint import pprint

def assign(boards, n, color):
    for k in range(5, -1, -1):
        if boards[k][n] == 0:
            boards[k][n] = color
            return

def crash(boards):
    def isInBound(_i, _j):
        if 0 <= _i < 6 and 0 <= _j < 6:
            return True
        return False

    def dfs(ci, cj, used, currArray):
        dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        currColor = boards[ci][cj]
        
        for d in dx:
            ni = ci + d[0]
            nj = cj + d[1]

            if isInBound(ni, nj) and not used[ni][nj] and boards[ni][nj] == currColor:
                used[ni][nj] = True
                currArray.append((ni, nj))
                dfs(ni, nj, used, currArray)
    
    _flag = False
    for i in range(6):
        for j in range(6):
            used = [[False for _ in range(6)] for _ in range(6)]
            currArray = []
            if boards[i][j] != 0:
                currArray = [(i, j)]
                used[i][j] = True
                dfs(i, j, used, currArray)

                # check
                if len(currArray) > 2:
                    _flag = True
                    for item in currArray:
                        ti, tj = item
                        boards[ti][tj] = 0
    return _flag
                


def down(boards):
    for i in range(5, -1, -1):
        for j in range(6):
            if boards[i][j] != 0:
                baseI = i
                ni = i + 1
                while ni < 6 and boards[ni][j] == 0:
                    boards[ni][j] = boards[baseI][j]
                    boards[baseI][j] = 0
                    baseI = ni
                    ni += 1
                    


def solution(macaron):
    boards = [[0 for _ in range(6)] for _ in range(6)]
    
    for num, color in macaron:
        assign(boards, num-1, color)

        flag = True
        while flag:
            flag = crash(boards)
            down(boards)

        
    res = ['' for _ in range(6)]
    for i in range(6):
        res[i] = ''.join(list(map(str, boards[i])))
    
    return res


# [num, color] 1번에 1번색, 2번에 1번색
macaron = [[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]]
print(solution(macaron))