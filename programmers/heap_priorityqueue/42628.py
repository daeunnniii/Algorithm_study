import heapq
def solution(operations):
    min_h, max_h = [], []
    for o in operations:
        op, n = o.split(' ')
        n = int(n)
        if op == "I":
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, -n)
        elif op == "D" and n == 1 and max_h:
            p = heapq.heappop(max_h)
            min_h.remove(-p)
        elif op == "D" and n == -1 and min_h:
            p = heapq.heappop(min_h)
            max_h.remove(-p)
    if min_h and max_h:
        min_p = heapq.heappop(min_h)
        max_p = heapq.heappop(max_h)
        return [-max_p, min_p]
    else:
        return [0, 0]