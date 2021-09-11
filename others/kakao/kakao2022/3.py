# 카카오 블라인드 2022 3번

import math


def timeToMin(t):
    hour, minute = t.split(':')
    return int(hour) * 60 + int(minute)


def caclDifference(records):
    stack = {}
    allTime = {}

    for record in records:
        time, carNum, flag = record
        carNum = int(carNum)

        if flag == 'IN':
            try:
                stack[carNum].append(time)
            except:
                stack[carNum] = [time]
        else:
            inTime = stack[carNum].pop()
            outTime = time
            diff = timeToMin(outTime) - timeToMin(inTime)

            try:
                allTime[carNum] += diff
            except:
                allTime[carNum] = diff

    for k, v in stack.items():
        if v:
            try:
                allTime[k] += 1439 - timeToMin(v.pop())
            except:
                allTime[k] = 1439 - timeToMin(v.pop())

    allTime = sorted(list(allTime.items()))
    return allTime


def calcFees(allTime, fees):
    res = []
    basicMin, basicFee, unitMin, unitFee = fees
    for times in allTime:
        t = times[1]
        if t <= basicMin:
            res.append(basicFee)
        else:
            uf = math.ceil((t - basicMin) / unitMin) * unitFee
            total = basicFee + uf
            res.append(total)
    return res


def solution(fees, records):
    for i in range(len(records)):
        records[i] = records[i].split()

    allTime = caclDifference(records)
    res = calcFees(allTime, fees)

    return res


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))
