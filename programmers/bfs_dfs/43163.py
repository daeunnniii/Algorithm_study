from collections import deque

def bfs(graph, start, visited, dis):
    queue = deque([start])
    dis[start] = 1
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                dis[i] = dis[v] + 1
                visited[i] = True
    return dis

def solution(begin, target, words):
    if target not in words:
        return 0
    start, word_graph = 0, {}
    for w in words:
        check_start = [begin[i]==w[i] for i in range(len(w))]
        if check_start.count(False)==1:
            start=w
        current_g = []
        w_list = list(words)
        w_list.remove(w)
        for w_l in w_list:
            check = [w[i]==w_l[i] for i in range(len(w))]
            if check.count(False)==1:
                current_g.append(w_l)
        word_graph[w] = current_g
    
    c_visited = {w: False for w in words}
    distance = {w: 0 for w in words}
    answer = bfs(word_graph, start, c_visited, distance)
    return answer[target]