import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start, costs):
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)
    for a, b, c in costs:
        graph[a].append((b, c))
        graph[b].append((a, c))
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

testcase = int(input())
answer = []
for i in range(testcase):
    input_costs, candidate = [], []
    n, m, t = map(int, input().split())
    start, g, h = map(int, input().split())

    for _ in range(m):
        a, b, d = map(int, input().split())
        input_costs.append([a, b, d])
        if (a==g and b==h) or (a==h and b==g):
            g_h = d
    for _ in range(t):
        candidate.append(int(input()))

    graph_1 = dijkstra(start, input_costs)
    graph_g = dijkstra(g, input_costs)
    graph_h = dijkstra(h, input_costs)

    current_answer = []
    for c in candidate:
        if graph_1[c] == (graph_1[g] + g_h + graph_h[c]) or graph_1[c] == (graph_1[h] + g_h + graph_g[c]):
            current_answer.append(c)
    current_answer.sort()
    answer.append(current_answer)

for a in answer:
    for p in a:
        print(p , end=" ")
    print()
