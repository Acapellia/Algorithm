import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m, start = map(int,input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x,y,w = map(int, input().split())
    graph[x].append((y,w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(start,0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))
dijkstra(start)

cnt = 0
time = 0
for d in range(1,len(distance)):
    if distance[d] != INF and d != start:
        cnt +=1
    if time < distance[d] and distance[d] != INF:
        time = distance[d]
print(cnt, time)
'''
3 2 1
1 2 4
1 3 2
'''