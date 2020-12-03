from collections import deque
def solution(priorities, location):
    queue = deque((j,i) for i, j in enumerate(priorities))
    answer = 0
    while queue:
 
        pop_number = queue.popleft()
        if queue and pop_number[0] < max(queue)[0]:
            queue.append(pop_number)
        else:
            answer += 1
            if location == pop_number[1]:
                return answer