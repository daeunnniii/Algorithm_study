def solution(numbers, target):
    graph = [[0]]
    for i in range(len(numbers)):
        current_s = []
        for g in graph[i]:
            current_s.append(g-numbers[i])
            current_s.append(g+numbers[i])
        graph.append(current_s)
    answer = graph[-1].count(target)
    return answer