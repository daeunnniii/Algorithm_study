from collections import deque
import sys
import copy
sys.setrecursionlimit(10**6)
i = 0
def bfs(graph, start, ticket):
    global i
    ret = []
    queue = deque([start])
    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        ret.append(v)
        if v not in graph.keys() or len(graph[v])==0:
            return (ret, len(ticket))
        if len(graph[v])>1:
            graph[v].sort()
            g_pop = graph[v].pop(i)
        else:    
            g_pop = graph[v].pop(0)
        queue.append(g_pop)
        
        ticket.remove([v, g_pop])


def solution(tickets):
    global i
    start = [t[0] for t in tickets]
    airport = {s:[] for s in set(start)}
    for t in tickets:
        airport[t[0]].append(t[1])
    answer = bfs(copy.deepcopy(airport), "ICN", list(tickets))
    while answer[1]>0:
        # print(answer)
        i+=1
        answer = bfs(copy.deepcopy(airport), "ICN", list(tickets))
    return answer[0]

pr = solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]])
