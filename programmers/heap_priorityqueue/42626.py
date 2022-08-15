from heapq import *
def solution(scoville, K):
    answer = 0
    heapify(scoville)
    s1 = heappop(scoville)
    while s1 < K:
        if len(scoville)==0:
            return -1
        answer += 1
        s2 = heappop(scoville)
        new_s = s1 + s2*2
        heappush(scoville, new_s)
        s1 = heappop(scoville)
    return answer