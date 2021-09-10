# 2020 카카오 블라인드
# 가사 검색
def setWordsLength(words, words_length, n):
    for i in range(n):
        words_length[i] = len(words[i])


def setQuery(queries, originQuery):
    for i in range(len(queries)):
        q = queries[i]
        qn = len(q)
        flag = False if q[0] == '?' else True
        originQuery[i] = [q.replace('?', ''), qn, flag]


def solution(words, queries):
    n = len(words)
    qn = len(queries)
    res = [0] * qn

    words_length = [0] * n
    setWordsLength(words, words_length, n)

    originQuery = [[]] * qn
    setQuery(queries, originQuery)

    for i in range(n):
        for j in range(qn):
            if words_length[i] == originQuery[j][1]:  # 길이 같으면
                w = originQuery[j][0]
                f = False
                if originQuery[j][2]:
                    f = words[i].startswith(w)
                else:
                    f = words[i].endswith(w)

                if f:
                    res[j] += 1

    return res


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
