from collections import deque
def bfs(group, visited):
    a = 0
    queue = deque()
    while not(all(visited)):
        index = visited.index(False)
        queue.append(index)
        visited[index] = True
        while queue:
            v = queue.popleft()
            for i in group[v]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)
        a += 1
    return a
                
def solution(n, computers):
    visited = [False]*n
    network = [list() for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if x==y:
                continue
            if computers[x][y]==1:
                network[x].append(y)
    answer = bfs(network, visited)
    return answer