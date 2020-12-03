import math
def solution(progresses, speeds):
    progresses = zip(progresses,speeds)
    remain_work = []
    stack = []
    count_list = []
    count = 0
    for work in progresses:
        remain_work.append(math.ceil((100 - work[0]) / work[1]))

    for work in range(len(remain_work)):
        if not stack:
            stack.append(remain_work[work])
            count += 1
        else:
            if stack[-1] >= remain_work[work]:
                count += 1
            else:
                stack.append(remain_work[work])
                count_list.append(count)
                count = 1
    count_list.append(count)

    return count_list