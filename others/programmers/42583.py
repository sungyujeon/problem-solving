# Programmers
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weights = 0
    truck_weights = deque(truck_weights)
    curr_on_bridge_trucks = deque([])

    while truck_weights or curr_on_bridge_trucks:
        setTimeOnBridgeTrucks(curr_on_bridge_trucks)
        removed_truck = removeTruck(curr_on_bridge_trucks, bridge_length)
        if removed_truck:
            total_weights -= removed_truck
        
        if truck_weights and weight >= total_weights + truck_weights[0]:
            curr_truck = truck_weights.popleft()
            total_weights += curr_truck
            curr_on_bridge_trucks.append([curr_truck, 1])
        
        time += 1
    return time

def setTimeOnBridgeTrucks(curr_on_bridge_trucks):
    n = len(curr_on_bridge_trucks)
    for i in range(n):
        curr_on_bridge_trucks[i][1] = curr_on_bridge_trucks[i][1] + 1

def removeTruck(curr_on_bridge_trucks, bridge_length):
    if not curr_on_bridge_trucks:
        return 0

    if curr_on_bridge_trucks[0][1] > bridge_length:
        truck_weight = curr_on_bridge_trucks.popleft()
        return truck_weight[0]
    return 0

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))
