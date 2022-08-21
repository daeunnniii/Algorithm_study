import math
def solution(progresses, speeds):
    answer, check=[], []
    for p, s in zip(progresses, speeds):
        remain = (100-p)/s
        check.append(math.ceil(remain))
    i, j = 0, 1
    while j<len(check):
        if check[i] < check[j]:
            answer.append(len(check[i:j]))
            i=j
        j += 1
    answer.append(len(check[i:]))
    return answer