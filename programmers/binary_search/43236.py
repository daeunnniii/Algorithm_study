def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end = 1, distance
    while start <= end:
        min_distance = int(1e9)
        current, remove = 0, 0
        mid = (start+end)//2
        for r in rocks:
            if r - current < mid:
                remove += 1
            else:
                min_distance = min(min_distance, r-current)
                current = r
        if remove <= n:
            answer = min_distance
            start = mid + 1
        else:
            end = mid - 1
    return answer