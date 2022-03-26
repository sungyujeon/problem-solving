def setSentences(sentences):
    new_sentences = []

    for sentence in sentences:
        n = len(sentence)
        word_set = set(list(sentence.replace(' ', '')))

        # find uppercase
        new_word_set = set([])
        upper_cnt = 0
        for word in word_set:
            char = ord(word)
            new_word_set.add(word.lower())
            if 65 <= char <= 90:
                upper_cnt += 1
                new_word_set.add('shift')
        new_sentences.append([new_word_set, n, n+upper_cnt, sentence])
    
    return new_sentences

def setUnion(sentences, N):
    union_dict = {}
    for i in range(N):
        union_dict[i] = []

    for i in range(N):
        for j in range(i+1, N):
            set_a = sentences[i][0]
            set_b = sentences[j][0]

            if set_b.issubset(set_a):
                union_dict[i].append(j)
            if set_a.issubset(set_b):
                union_dict[j].append(i)
    return union_dict
    
def setVisited(visited, children):
    for c in children:
        visited[c] = True

def dfs(sentences, visited, union, N, curr_n, curr_score):
    global answer 

    for i in range(N):
        if not visited[i] and sentences[i][1] <= curr_n:
            _, _length, _score, _ = sentences[i]
            visited[i] = True
            curr_score += _score
            children_idx = union[i]
            for c_idx in children_idx:
                if not visited[c_idx]:
                    visited[c_idx] = True
                    c_score = sentences[c_idx][2]
                    curr_score += c_score
            
            # check
            if answer < curr_score:
                answer = curr_score

            dfs(sentences, visited, union, N, curr_n-_length, curr_score)
            visited[i] = False
            curr_score -= _score
            for c_idx in children_idx:
                visited[c_idx] = False
                c_score = sentences[c_idx][2]
                curr_score -= c_score
        
answer = -1
def solution(sentences, n):
    global answer

    N = len(sentences)
    sentences = setSentences(sentences)

    # union
    union = setUnion(sentences, N)
    
    # calc
    visited = [False] * N
    dfs(sentences, visited, union, N, n, 0)   

    return answer

sentences = ["a", "b", "c", "d"]
n = 4
print(solution(sentences, n))






# for i in range(N):
#     tmp_n = n
#     tmp_score = 0
#     visited = [False] * N
#     parent_idx = i
#     children_idx = union[parent_idx]
#     setVisited(visited, parent_idx, children_idx)

#     # parent + children score
#     _, length, score, _ = sentences[parent_idx]
#     if length <= tmp_n:
#         tmp_n -= length
#         tmp_score += score
#         for c_idx in children_idx:
#             tmp_score += sentences[c_idx][2]
        
#         # check
#         if answer < tmp_score:
#             answer = tmp_score
#     else:
#         continue
    
    # dfs()
    # for j in range(N):
    #     if not visited[j] and sentences[j][1] <= tmp_n:
    #         visited[j] = True