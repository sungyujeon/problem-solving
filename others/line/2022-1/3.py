def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    N = len(employees)
    remote_tasks = set(remote_tasks)
    office_tasks = set(office_tasks)
    teams = [[] for _ in range(num_teams)]
    office_teams = [[] for _ in range(num_teams)]
    remote_teams = [[] for _ in range(num_teams)]

    for i in range(N):
        numAndTasks = employees[i].split()
        num = int(numAndTasks[0]) - 1
        tasks = numAndTasks[1:]
        
        # add empId to teams
        teams[num].append(i+1)

        # tasks
        remote_flag = True
        for task in tasks:
            if task in office_tasks:
                remote_flag = False
                break
        if remote_flag:
            remote_teams[num].append(i+1)
        else:
            office_teams[num].append(i+1)
    
    for i in range(num_teams):
        if not office_teams[i]:
            remote_teams[i].pop(0)

    for t in remote_teams:
        answer += t

    return answer


num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]

print(solution(num_teams, remote_tasks, office_tasks, employees))