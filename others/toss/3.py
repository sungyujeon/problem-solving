# 조직도 검색하기


def getChildren(id, hierachy_dict):
    ids = [id]
    children = set([])

    while ids:
        _id = ids.pop()

        ch = hierachy_dict.get(_id)
        if ch != None:
            children = children | ch
            ids.extend(list(ch))

    return children


def arrange_team(team, hierachy_dict, name_id_dict):
    [orgId, orgName, higherOrgId, memberCnt] = team

    # hierachy
    if hierachy_dict.get(higherOrgId) == None:
        hierachy_dict[higherOrgId] = set([orgId])
    else:  # 있으면
        hierachy_dict[higherOrgId].add(orgId)

    # name
    name_id_dict[orgName] = orgId


def solution(csv_string, keyword):
    hierachy_dict = {}
    name_id_dict = {}
    names = []
    members = {}
    total = 0

    # arrange
    myInput = csv_string.split("\n")
    for _input in myInput[1:]:
        team = _input.split(",")
        members[team[0]] = team[3]
        names.append(team[1])
        arrange_team(team, hierachy_dict, name_id_dict)

    # search
    id_list = set([])
    if keyword == "":  # 전체 검색
        id_list = set(members.keys())
    else:
        for name in names:
            if name.find(keyword) != -1:
                id_list.add(name_id_dict.get(name))

        # calc
        for myId in id_list:
            myChildren = getChildren(myId, hierachy_dict)
            if myChildren:
                id_list = id_list | myChildren

    # calc
    if not id_list:
        return -1
    else:
        for myId in id_list:
            total += int(members[myId])

    return total


csv_string = "조직 ID,조직명,상위 조직 ID,소속 팀원 수\n1,토스팀,,1\n2,인터널 트라이브,1,1\n3,인터널 매니저 팀,2,7\n4,비바 플랫폼 팀,2,14\n5,아웃터널 트라이브,1,2\n6,가이드 팀,5,4\n7,피트아웃 사일로,5,11"
keyword = "트라이브"

print(solution(csv_string, keyword))
