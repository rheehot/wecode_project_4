def solution(bridge_length, weight, truck_weights):
    crossing = []
    finish = []
    count_list = []
    count  = 1
     
    while crossing or truck_weights:
        if not crossing:
            crossing.append(truck_weights.pop(0))
            count_list.append(1)

        if count_list and count_list[0] == bridge_length :
            finish.append(crossing.pop(0))
            count_list.pop(0)

        if truck_weights and sum(crossing) + truck_weights[0] <= weight:
            crossing.append(truck_weights.pop(0))
            for i in range(len(count_list)):
                count_list[i] = count_list[i] + 1
            count_list.append(1)
            count += 1
        else:
            count += 1
            for i in range(len(count_list)):
                count_list[i] = count_list[i] + 1
        
       
    return count

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))