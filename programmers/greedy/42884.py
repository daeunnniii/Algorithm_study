def solution(routes):
    answer = 0
    while routes:
        min_end = min(routes, key=lambda x:x[1])[1]
        check_lst = []
        for r in routes:
            if r[0] > min_end or r[1] < min_end:
                check_lst.append(r)
        routes = list(check_lst)
        answer += 1
    return answer