# 라인 공채 2021 3번

# 닉네임 / 이메일 주소 모두 유사하면 동일 유저
# a, b / b, c 동일 시 a, c 동일
# 총 2개 이하 문자 삭제 후 동일하게 만들면 유사
# 이메일 계쩡 이름 동일 시 서버 이름 상관없이 유사
# unique 유저 수 리턴

def isNickSimilar(nick1, nick2):
    len1 = len(nick1)
    len2 = len(nick2)

    if len1 < len2:
        nick1, nick2 = nick2, nick1
        len1, len2 = len2, len1

    # nick1이 삭제
    nick2 += ' ' * (len1 - len2)
    i = 0
    j = 0
    tmpCheck = 0
    while i < len1:
        if nick1[i] != nick2[j]:
            tmpCheck += 1
            if tmpCheck > 2:
                return False
            i += 1
        else:
            i += 1
            j += 1
    if len2 - j > 2 - tmpCheck:
        return False
    return True


def isEmailSimilar(email1, email2):
    def isEmailNameSimilar(name1, name2):
        len1 = len(name1)
        len2 = len(name2)

        if abs(len1 - len2) != 1:
            return False
        else:
            n1 = name1.split()
            n2 = name2.split()
            if len1 < len2:
                name1, name2 = name2, name1

            name2 += ' '
            i = 0
            j = 0
            tmp = 0
            while i < len(name1):
                if name1[i] != name2[j]:
                    tmp += 1
                    if tmp > 1:
                        return False
                    i += 1
                else:
                    i += 1
                    j += 1
            return True

    name1, server1 = email1.split('@')
    name2, server2 = email2.split('@')

    if name1 == name2:
        return True
    else:
        if server1 != server2:
            return False
        else:
            return isEmailNameSimilar(name1, name2)


def isSimilar(i, j, nicks, emails):
    nick1 = nicks[i]
    nick2 = nicks[j]
    email1 = emails[i]
    email2 = emails[j]

    r1 = isNickSimilar(nick1, nick2)
    r2 = isEmailSimilar(email1, email2)

    return r1 and r2


def getParents(pa, node):
    while pa[node] != node:
        node = pa[node]
    return node


def solution(nicks, emails):
    n = len(nicks)
    nodes = []
    for i in range(n-1):
        for j in range(i+1, n):
            flag = isSimilar(i, j, nicks, emails)
            if flag:
                nodes.append([i, j])

    pa = [i for i in range(n)]
    res = [[] for i in range(n)]
    for node in nodes:
        parentNode, childNode = node
        pa[childNode] = parentNode
        p = getParents(pa, parentNode)
        res[p].append(childNode)

    used = [False for _ in range(n)]
    for i in range(n):
        for j in range(len(res[i])):
            used[res[i][j]] = True
            used[i] = True

    total = 0
    for t in used:
        if not t:
            total += 1
    for r in res:
        if r:
            total += 1

    return total


nicks = ["imhero111", "moneyman", "hero111",
         "imher1111", "hro111", "mmoneyman", "moneymannnn"]
emails = ["superman5@abcd.com", "batman432@korea.co.kr", "superman@abcd.com",
          "supertman5@abcd.com", "superman@erty.net", "batman42@korea.co.kr", "batman432@usa.com"]

# nicks = ["99police", "99poli44"]
# emails = ["687ufq687@aaa.xx.yyy", "87ufq687@aaa.xx.yyy"]
print(solution(nicks, emails))
