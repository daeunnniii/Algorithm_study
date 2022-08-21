from heapq import *

def solution(jobs):
    check = []
    current_t, sum_t, len_j = 0, 0, len(jobs)
    heapify(jobs)
    while jobs:
        while jobs and jobs[0][0] <= current_t:
            request, time = heappop(jobs)
            heappush(check, [time, request])
        if check:
            t, r = heappop(check)
            current_t += t
            sum_t += current_t - r
        else:
            current_t += 1
    while check:
        t, r = heappop(check)
        current_t += t
        sum_t += current_t - r
    return sum_t//len_j