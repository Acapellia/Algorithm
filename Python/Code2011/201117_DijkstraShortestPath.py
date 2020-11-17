import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
start = int(input())
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
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''