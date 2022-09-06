import heapq
def dijkstra(graph, start, distance):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

INF = int(1e9)
N, M, X = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
distance = [INF] * (1+N)
answer = [0] * (N+1)
for m in range(M):
    a, b, c = map(int, input().split(' '))
    graph[a].append([b, c])
for i in range(1, N+1):
    distance = [INF] * (1+N)
    dijkstra(graph, i, distance)
    answer[i] += distance[X]
distance = [INF] * (1+N)
dijkstra(graph, X, distance)
for i in range(1, N+1):
    answer[i] += distance[i]
print(max(answer))


